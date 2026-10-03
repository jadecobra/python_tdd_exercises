import streamlit


def show_number(display):
    display.write(streamlit.session_state['number'])


def plus_minus():
    if streamlit.session_state['number'].startswith('-'):
        number = streamlit.session_state['number'][1:]
    else:
        number = '-' + streamlit.session_state['number']
    streamlit.session_state['number'] = number


def backspace():
    number = streamlit.session_state['number'][:-1]
    streamlit.session_state['number'] = number


def add_decimal():
    if streamlit.session_state['number'].count('.') == 0:
        streamlit.session_state['number'] += '.'


def add_number_to_state(number):
    if streamlit.session_state['number'] == '0':
        streamlit.session_state['number'] = number
    else:
        streamlit.session_state['number'] += number


def on_click(function, display, *value):
    function(*value)
    show_number(display)


def add_buttons_to_column_1(column_1, display):
    column_1.button(
        label='<-', key='<-', width='stretch', on_click=on_click,
        args=[backspace, display],
    )
    column_1.button(
        label='7', key='7', width='stretch', on_click=on_click,
        args=[add_number_to_state, display, '7'],
    )
    column_1.button(
        label='4', key='4', width='stretch', on_click=on_click,
        args=[add_number_to_state, display, '4'],
    )
    column_1.button(
        label='1', key='1', width='stretch', on_click=on_click,
        args=[add_number_to_state, display, '1'],
    )
    column_1.button(
        label='+/-', key='+/-', width='stretch', on_click=on_click,
        args=[plus_minus, display],
    )


def add_buttons_to_column_2(column_2, display):
    column_2.button(
        label='C', key='C', width='stretch', type='primary',
    )
    column_2.button(
        label='8', key='8', width='stretch', on_click=on_click,
        args=[add_number_to_state, display, '8'],
    )
    column_2.button(
        label='5', key='5', width='stretch', on_click=on_click,
        args=[add_number_to_state, display, '5'],
    )
    column_2.button(
        label='2', key='2', width='stretch', on_click=on_click,
        args=[add_number_to_state, display, '2'],
    )
    column_2.button(
        label='0', key='0', width='stretch', on_click=on_click,
        args=[add_number_to_state, display, '0'],
    )


def add_buttons_to_column_3(column_3, display):
    column_3.button(
        label='AC', key='AC', width='stretch', type='primary',
    )
    column_3.button(
        label='9', key='9', width='stretch', on_click=on_click,
        args=[add_number_to_state, display, '9'],
    )
    column_3.button(
        label='6', key='6', width='stretch', on_click=on_click,
        args=[add_number_to_state, display, '6'],
    )
    column_3.button(
        label='3', key='3', width='stretch', on_click=on_click,
        args=[add_number_to_state, display, '3'],
    )
    column_3.button(
        label='.', key='.', width='stretch', on_click=on_click,
        args=[add_decimal, display]
    )


def add_buttons_to_column_4(column_4):
    column_4.button(
        label='/', key='/', width='stretch', type='primary',
    )
    column_4.button(
        label='X', key='X', width='stretch', type='primary',
    )
    column_4.button(
        label=r'\-', key=r'\-', width='stretch', type='primary',
    )
    column_4.button(
        label=r'\+', key=r'\+', width='stretch', type='primary',
    )
    column_4.button(
        label='=', key='=', width='stretch', type='primary',
    )


def main():
    streamlit.title('Calculator')
    streamlit.session_state.setdefault('number', '0')
    display = streamlit.container(border=True)

    column_1, column_2, column_3, operations = streamlit.columns(4)
    add_buttons_to_column_1(column_1, display)
    add_buttons_to_column_2(column_2, display)
    add_buttons_to_column_3(column_3, display)
    add_buttons_to_column_4(operations)


if __name__ == '__main__':
    main()