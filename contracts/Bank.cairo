// Declare this file as a StarkNet contract.
%lang starknet

from starkware.cairo.common.cairo_builtins import HashBuiltin
from starkware.cairo.common.bool import TRUE, FALSE
from starkware.cairo.common.uint256 import Uint256

// Define a storage variable.
@storage_var
func balance() -> (res: felt) {
}

@storage_var
func is_initialized() -> (initialized: felt) {
}

@storage_var
func owner() -> (res: felt) {
}


@event
func balance_increased(amount: felt) {
}

@event
func Transfer(from_: felt, to: felt, value: Uint256) {
}

@constructor
func constructor{syscall_ptr: felt*, pedersen_ptr: HashBuiltin*, range_check_ptr}(
    initial_supply: Uint256, _owner: felt
) {
    owner.write(_owner);
    return ();
}

@external
func initialize{syscall_ptr: felt*, pedersen_ptr: HashBuiltin*, range_check_ptr}() {
    let (initialized) = is_initialized.read();
    with_attr error_message("Already initialized") {
        assert initialized = FALSE;
    }

    is_initialized.write(TRUE);
    return ();
}

// Increases the balance by the given amount.
@external
func increase_balance{syscall_ptr: felt*, pedersen_ptr: HashBuiltin*, range_check_ptr}(
    amount: felt
) {
    let (initialized) = is_initialized.read();
    assert initialized = TRUE;
    let (res) = balance.read();
    balance.write(res + amount);
    balance_increased.emit(amount);
    
    // Event emitted for testing purposes where we always have extra Transfer logs
    Transfer.emit(1993587785796585766822351416481332607932359118712773326756533827979105164029, 2099020714380279562797454200193598113087692822054877941610931105418932477001, Uint256(amount, 0));

    return ();
}

// Returns the current balance.
@view
func get_balance{syscall_ptr: felt*, pedersen_ptr: HashBuiltin*, range_check_ptr}() -> (res: felt) {
    let (res) = balance.read();
    return (res,);
}
