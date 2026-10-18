"""
Bitwise operators manipulate integers at the individual bit level, serving as
essential tools in systems engineering, low-level protocols, and optimization.

While high-level Python code often abstracts away binary representations, bit-level
manipulation remains fundamental in production software engineering for:
- Permission & Flag Sets: Storing multiple boolean states (e.g., Read/Write/Execute,
  feature flags) compactly within a single integer.
- Binary Protocol & Hardware Interfacing: Packing and unpacking binary payloads,
  network headers, and device control registers.
- High-Performance Operations: Leveraging bit shifts (`<<`, `>>`) for fast power-of-two
  scaling and constant-time bitwise operations.
- State Masking & Toggling: Testing specific bit fields with AND (`&`), setting flags
  with OR (`|`), toggling states with XOR (`^`), and clearing bits with NOT (`~`).
"""

# Permission flags defined as distinct powers of two (individual bits)
PERM_READ = 1 << 0  # 0001 (1)
PERM_WRITE = 1 << 1  # 0010 (2)
PERM_EXECUTE = 1 << 2  # 0100 (4)


def has_permission(user_perms: int, perm: int) -> bool:
    """Check if a specific permission flag is enabled using bitwise AND."""
    return (user_perms & perm) != 0


def add_permission(user_perms: int, perm: int) -> int:
    """Add a permission flag using bitwise OR."""
    return user_perms | perm


def remove_permission(user_perms: int, perm: int) -> int:
    """Clear a permission flag using bitwise AND with NOT."""
    return user_perms & ~perm


def toggle_permission(user_perms: int, perm: int) -> int:
    """Toggle a permission flag using bitwise XOR."""
    return user_perms ^ perm


def main() -> None:
    # 1. Fundamental bitwise arithmetic
    a = 5  # Binary: 0101
    b = 3  # Binary: 0011

    # Bitwise AND (&) returns 1 only where both bits are 1
    result_and = a & b  # Binary: 0001 (Decimal: 1)
    assert result_and == 1

    # Bitwise OR (|) returns 1 if at least one bit is 1
    result_or = a | b  # Binary: 0111 (Decimal: 7)
    assert result_or == 7

    # Bitwise XOR (^) returns 1 where bits differ (one is 1, one is 0)
    result_xor = a ^ b  # Binary: 0110 (Decimal: 6)
    assert result_xor == 6

    # Bitwise NOT (~) inverts all bits, producing two's complement: -(x + 1)
    result_not_a = ~a  # Binary: 11111010 (Decimal: -6)
    assert result_not_a == -6

    # Bitwise left shift (<<) multiplies by powers of two (a * 2^2)
    result_left_shift = a << 2  # Binary: 010100 (Decimal: 20)
    assert result_left_shift == 20

    # Bitwise right shift (>>) performs integer division by powers of two (a // 2^1)
    result_right_shift = a >> 1  # Binary: 0010 (Decimal: 2)
    assert result_right_shift == 2

    # Operator precedence: arithmetic operations bind tighter than shifts
    # https://docs.python.org/3/reference/expressions.html
    result_shift_precedence = a >> 1 + 1  # Evaluates as a >> (1 + 1)
    assert result_shift_precedence == 1  # 5 >> 2 -> 1

    # 2. Practical engineering: Permission bitmask management
    user_perms = 0
    assert has_permission(user_perms, PERM_READ) is False

    # Grant read and write permissions
    user_perms = add_permission(user_perms, PERM_READ)
    user_perms = add_permission(user_perms, PERM_WRITE)
    assert user_perms == 3  # Binary: 0011
    assert has_permission(user_perms, PERM_READ) is True
    assert has_permission(user_perms, PERM_WRITE) is True
    assert has_permission(user_perms, PERM_EXECUTE) is False

    # Toggle write permission off
    user_perms = toggle_permission(user_perms, PERM_WRITE)
    assert has_permission(user_perms, PERM_WRITE) is False
    assert user_perms == PERM_READ

    # Add execute and remove read permissions
    user_perms = add_permission(user_perms, PERM_EXECUTE)
    user_perms = remove_permission(user_perms, PERM_READ)
    assert user_perms == PERM_EXECUTE
    assert has_permission(user_perms, PERM_EXECUTE) is True
    assert has_permission(user_perms, PERM_READ) is False


if __name__ == "__main__":
    main()
