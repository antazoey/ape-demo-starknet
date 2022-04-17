# Declare this file as a StarkNet contract.
%lang starknet

from starkware.cairo.common.cairo_builtins import HashBuiltin
from starkware.cairo.common.bool import TRUE, FALSE

# Define a storage variable.
@storage_var
func balance() -> (res : felt):
end

@storage_var
func is_initialized() -> (initialized: felt):
end

@event
func balance_increased(amount : felt):
end

@external
func initialize{
        syscall_ptr: felt*,
        pedersen_ptr: HashBuiltin*,
        range_check_ptr
    }():
    let (initialized) = is_initialized.read()
    with_attr error_message("Already initialized"):
        assert initialized = FALSE
    end

    is_initialized.write(TRUE)
    return ()
end

# Increases the balance by the given amount.
@external
func increase_balance{
        syscall_ptr : felt*, pedersen_ptr : HashBuiltin*,
        range_check_ptr}(amount : felt):
    let (initialized) = is_initialized.read()
    assert initialized = TRUE
    let (res) = balance.read()
    balance.write(res + amount)
    balance_increased.emit(amount)
    return ()
end

# Returns the current balance.
@view
func get_balance{
        syscall_ptr : felt*, pedersen_ptr : HashBuiltin*,
        range_check_ptr}() -> (res : felt):
    let (res) = balance.read()
    return (res)
end
