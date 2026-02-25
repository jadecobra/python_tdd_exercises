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
    streamlit.session_state['number'] = '0'
    container.write(streamlit.session_state['number'])


def backspace(container, *args):
    streamlit.session_state['number'] = streamlit.session_state['number'][:-1]
    container.write(streamlit.session_state['number'])


def show(container, value):
    update_state(value)
    container.write(streamlit.session_state['number'])


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


def main():
    streamlit.title('Calculator')
    streamlit.session_state.setdefault('number', '0')
    operations = {
        '+': calculator.add,
        '-': calculator.subtract,
        '/': calculator.divide,
        'x': calculator.multiply,
    }

    display = streamlit.container(border=True)

    col_1, col_2, col_3, operations = streamlit.columns(4, vertical_alignment='bottom')

    operations.button('/', type='primary', width='stretch')
    operations.button('X', type='primary', width='stretch')
    operations.button('\-', type='primary', width='stretch')
    operations.button('\+ ', type='primary', width='stretch')
    operations.button('=', type='primary', width='stretch')

    add_button('AC', col_3, type='primary', on_click=reset_state, display=display)
    add_button('9', col_3, on_click=show, display=display)
    add_button('6', col_3, on_click=show, display=display)
    add_button('3', col_3, on_click=show, display=display)
    add_button('.', col_3, on_click=show, display=display)

    add_button('C', col_2, type='primary', on_click=reset_state, display=display)
    add_button('8', col_2, on_click=show, display=display)
    add_button('5', col_2, on_click=show, display=display)
    add_button('2', col_2, on_click=show, display=display)
    add_button('0', col_2, on_click=show, display=display)

    add_button('<-', col_1, on_click=backspace, display=display)
    add_button('7', col_1, on_click=show, display=display)
    add_button('4', col_1, on_click=show, display=display)
    add_button('1', col_1, on_click=show, display=display)
    add_button('+/-', col_1, on_click=show, display=display)


if __name__ == '__main__':
    main()