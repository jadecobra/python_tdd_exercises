import streamlit


def show_result(display):
    streamlit.session_state['second_number'] = \
        streamlit.session_state['number']
    streamlit.session_state['number'] = str(
        float(streamlit.session_state['first_number'])
      + float(streamlit.session_state['second_number'])
    )
    display.write(streamlit.session_state['number'])


def make_variable(display):
    streamlit.session_state['first_number'] = \
        streamlit.session_state['number']
    reset_state(display)


def reset_state(display):
    streamlit.session_state['number'] = '0'
    display.write(streamlit.session_state['number'])


def update_state(value):
    if value == '.':
        if (
            streamlit.session_state['number']
            .count('.') != 0
        ):
            return
    if streamlit.session_state['number'] == '0':
        streamlit.session_state['number'] = value
        return
    if value == '+/-':
        if not (
            streamlit.session_state['number']
            .startswith('-')
        ):
            negative = (
                '-'  +
                streamlit.session_state['number']
            )
            streamlit.session_state['number'] = \
                negative
            return
        else:
            streamlit.session_state['number'] = \
                streamlit.session_state['number'][1:]
            return
    streamlit.session_state['number'] += value


def show(display, value):
    update_state(value)
    display.write(streamlit.session_state['number'])


def add_buttons():
    display = streamlit.container(border=True)
    column_1, column_2, column_3, operations = streamlit.columns(4)

    column_1.button('<-', key='<-', width='stretch')
    column_1.button(
        '7', key='7', width='stretch',
        on_click=show, args=[display, '7'],
    )
    column_1.button(
        '4', key='4', width='stretch',
        on_click=show, args=[display, '4'],
    )
    column_1.button(
        '1', key='1', width='stretch',
        on_click=show, args=[display, '1'],
    )
    column_1.button(
        '+/-', key='+/-', width='stretch',
        on_click=show, args=[display, '+/-'],
    )

    column_2.button(
        'C', key='C', width='stretch', type='primary',
        on_click=reset_state, args=[display],
    )
    column_2.button(
        '8', key='8', width='stretch',
        on_click=show, args=[display, '8'],
    )
    column_2.button(
        '5', key='5', width='stretch',
        on_click=show, args=[display, '5'],
    )
    column_2.button(
        '2', key='2', width='stretch',
        on_click=show, args=[display, '2'],
    )
    column_2.button(
        '0', key='0', width='stretch',
        on_click=show, args=[display, '0'],
    )

    column_3.button(
        'AC', key='AC', width='stretch', type='primary',
        on_click=reset_state, args=[display],
    )
    column_3.button(
        '9', key='9', width='stretch',
        on_click=show, args=[display, '9'],
    )
    column_3.button(
        '6', key='6', width='stretch',
        on_click=show, args=[display, '6'],
    )
    column_3.button(
        '3', key='3', width='stretch',
        on_click=show, args=[display, '3'],
    )
    column_3.button(
        '.', key='.', width='stretch',
        on_click=show, args=[display, '.'],
    )

    operations.button('/', key='/', width='stretch', type='primary')
    operations.button('X', key='X', width='stretch', type='primary')
    operations.button(r'\-', key='-', width='stretch', type='primary')
    operations.button(
        r'\+', key='+', width='stretch', type='primary',
        on_click=make_variable, args=[display],
    )
    operations.button(
        '=', key='=', width='stretch', type='primary',
        on_click=show_result, args=[display],
    )


def main():
    streamlit.title('Calculator')
    streamlit.session_state.setdefault('number', '0')
    add_buttons()


if __name__ == '__main__':
    main()