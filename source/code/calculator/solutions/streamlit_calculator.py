import streamlit
import calculator


def update_state(value):
    if value == '.':
        if streamlit.session_state.number.count('.') == 0:
            streamlit.session_state.number += value
        if streamlit.session_state.number.count('.') != 0:
            return
    if streamlit.session_state.number == '0':
        streamlit.session_state.number = value
        return
    if value == '+/-':
        if streamlit.session_state.number.startswith('-'):
            streamlit.session_state.number = streamlit.session_state.number[1:]
            return
        if not streamlit.session_state.number.startswith('-'):
            new_number = '-' + streamlit.session_state.number
            streamlit.session_state.number = new_number
            return
    streamlit.session_state.number += value


def reset_state(container, *args):
    streamlit.session_state.number = '0'
    container.write(streamlit.session_state.number)


def backspace(container, *args):
    streamlit.session_state.number = streamlit.session_state.number[:-1]
    container.write(streamlit.session_state.number)


def show(container, value):
    update_state(value)
    container.write(streamlit.session_state.number)


def add_button(
        value, container=None, type='secondary', on_click=None, display=None
    ):
    container.button(
        value,
        type=type,
        width='stretch',
        on_click=on_click,
        args=[display, value]
    )

def make_variables(container, operation):
    streamlit.session_state.operation = operation
    first_number = streamlit.session_state.number
    reset_state(container)
    if streamlit.session_state.first_number:
        streamlit.session_state.second_number = streamlit.session_state.number
    container.write(f'{first_number} {operation} {streamlit.session_state.second_number} = ')

def get_result(operation, first_number, second_number):
    return {
        '\+': calculator.add,
        '\-': calculator.subtract,
        '/': calculator.divide,
        '\*': calculator.multiply,
    }[operation](
        float(first_number),
        float(second_number)
    )

def show_result(container, *args):
    streamlit.session_state.second_number = streamlit.session_state.number
    result = get_result(
        operation=streamlit.session_state.operation,
        first_number=streamlit.session_state.first_number,
        second_number=streamlit.session_state.second_number,
    )
    container.write(str(result))
    reset_state(container)


def main():
    streamlit.title('Calculator')
    streamlit.session_state.setdefault('number', '0')
    streamlit.session_state.setdefault('first_number', '0')
    streamlit.session_state.setdefault('second_number', '0')
    streamlit.session_state.setdefault('operation', '+')

    display = streamlit.container(border=True)

    column_1, column_2, column_3, operation = streamlit.columns(
        4, vertical_alignment='bottom'
    )

    add_button('/', operation, type='primary', on_click=make_variables, display=display)
    add_button('\*', operation, type='primary', on_click=make_variables, display=display)
    add_button('\-', operation, type='primary', on_click=make_variables, display=display)
    add_button('\+', operation, type='primary', on_click=make_variables, display=display)
    add_button('=', operation, type='primary', on_click=show_result, display=display)

    add_button('AC', column_3, type='primary', on_click=reset_state, display=display)
    add_button('9', column_3, on_click=show, display=display)
    add_button('6', column_3, on_click=show, display=display)
    add_button('3', column_3, on_click=show, display=display)
    add_button('.', column_3, on_click=show, display=display)

    add_button('C', column_2, type='primary', on_click=reset_state, display=display)
    add_button('8', column_2, on_click=show, display=display)
    add_button('5', column_2, on_click=show, display=display)
    add_button('2', column_2, on_click=show, display=display)
    add_button('0', column_2, on_click=show, display=display)

    add_button('<-', column_1, on_click=backspace, display=display)
    add_button('7', column_1, on_click=show, display=display)
    add_button('4', column_1, on_click=show, display=display)
    add_button('1', column_1, on_click=show, display=display)
    add_button('+/-', column_1, on_click=show, display=display)


if __name__ == '__main__':
    main()