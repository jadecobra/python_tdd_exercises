import streamlit as st
import src.calculator as calc


def main():
    st.title("🧮 My TDD Calculator")
    st.markdown("**Built step-by-step with Test-Driven Development** (Chapters 1–10)")

    # Layout: nice columns
    col1, col2, col3 = st.columns([3, 1, 3])

    with col1:
        first = st.number_input(
            "First number",
            value=0.0,
            step=0.1,
            format="%.4f"
        )

    with col2:
        operation = st.selectbox(
            "Operation",
            ["+", "-", "×", "÷"],
            index=0
        )

    with col3:
        second = st.number_input(
            "Second number",
            value=0.0,
            step=0.1,
            format="%.4f"
        )

    # Big calculate button
    if st.button("Calculate", type="primary", use_container_width=True):
        try:
            ops = {
                "+": calc.add,
                "-": calc.subtract,
                "×": calc.multiply,
                "÷": calc.divide
            }

            result = ops[operation](first, second)

            st.success(f"**{first} {operation} {second} = {result}**")

            # Save to history
            if "history" not in st.session_state:
                st.session_state.history = []

            st.session_state.history.append(
                f"{first} {operation} {second} = {result}"
            )

        except ZeroDivisionError:
            st.error("brmph?! I cannot divide by 0. Try again...")
        except Exception:
            st.error("brmph?! Numbers only. Try again...")

    # Show recent calculations
    if "history" in st.session_state and st.session_state.history:
        st.subheader("🕒 Recent calculations")
        for item in reversed(st.session_state.history[-10:]):
            st.write(item)

    if st.button("Clear history"):
        st.session_state.history = []


if __name__ == "__main__":
    main()