import math
import time


def star_delta_simulator():
    print("=" * 60)
    print("          STAR-DELTA STARTER SIMULATOR")
    print("=" * 60)

    # User inputs
    line_voltage = float(input("Enter line voltage (V): "))
    motor_power = float(input("Enter motor power (kW): "))
    efficiency = float(input("Enter motor efficiency (%): "))
    power_factor = float(input("Enter power factor: "))
    motor_current = float(input("Enter rated motor current (A): "))
    start_time = float(input("Enter star starting time (seconds): "))

    if line_voltage <= 0:
        print("Voltage must be greater than zero.")
        return

    if motor_power <= 0:
        print("Motor power must be greater than zero.")
        return

    if not 0 < efficiency <= 100:
        print("Efficiency must be between 0 and 100%.")
        return

    if not 0 < power_factor <= 1:
        print("Power factor must be between 0 and 1.")
        return

    if motor_current <= 0:
        print("Motor current must be greater than zero.")
        return

    if start_time < 0:
        print("Starting time cannot be negative.")
        return

    # Convert efficiency to decimal
    efficiency_decimal = efficiency / 100

    # Calculate input power
    input_power = motor_power * 1000 / efficiency_decimal

    # Theoretical three-phase current
    calculated_current = (
        input_power /
        (math.sqrt(3) * line_voltage * power_factor)
    )

    # Star connection
    star_phase_voltage = line_voltage / math.sqrt(3)

    # Approximate star starting current
    star_current = motor_current / 3

    # Delta current
    delta_current = motor_current

    print("\n" + "-" * 60)
    print("MOTOR PARAMETERS")
    print("-" * 60)

    print(f"Line Voltage          : {line_voltage:.2f} V")
    print(f"Motor Power           : {motor_power:.2f} kW")
    print(f"Efficiency            : {efficiency:.2f} %")
    print(f"Power Factor          : {power_factor:.2f}")
    print(f"Rated Motor Current   : {motor_current:.2f} A")
    print(f"Calculated Current     : {calculated_current:.2f} A")

    print("\n" + "-" * 60)
    print("STAR CONNECTION")
    print("-" * 60)

    print(f"Line Voltage          : {line_voltage:.2f} V")
    print(f"Phase Voltage         : {star_phase_voltage:.2f} V")
    print(f"Approx. Starting Current: {star_current:.2f} A")

    print("\nStarting motor in STAR mode...")

    for second in range(1, int(start_time) + 1):
        print(f"  STAR operation: {second} second(s)")
        time.sleep(1)

    print("\n" + "-" * 60)
    print("TRANSITION")
    print("-" * 60)

    print("STAR contactor OFF")
    print("Short transition period...")
    time.sleep(1)
    print("DELTA contactor ON")

    print("\n" + "-" * 60)
    print("DELTA CONNECTION")
    print("-" * 60)

    print(f"Phase Voltage         : {line_voltage:.2f} V")
    print(f"Running Current       : {delta_current:.2f} A")
    print("Motor Status          : RUNNING")
    print("Starter Mode          : DELTA")

    print("\n" + "-" * 60)
    print("RESULT")
    print("-" * 60)

    current_reduction = (
        (delta_current - star_current)
        / delta_current
    ) * 100

    print(f"Star Starting Current : {star_current:.2f} A")
    print(f"Delta Current         : {delta_current:.2f} A")
    print(f"Starting Current Reduction: {current_reduction:.2f}%")

    print("\nMotor successfully transitioned from STAR to DELTA.")

    print("=" * 60)


if __name__ == "__main__":
    star_delta_simulator()
