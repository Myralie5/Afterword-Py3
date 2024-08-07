label truename:
    $ user =''
    $ renpy.call_screen("name_input", "What should we call you?", ok_action=Jump("process_truename"), output_var="user")

label process_truename:
    if not user:
        jump truename
    return

label ch01_main:
    return

label authorchan:
    d "Whoops."
    d "The version of the game you're playing is {i}unfinished.{/i}"
    show sayori 1 at t11
    s "*le gasp* Author-chan!!!"
    s "You're not done?!?"
    menu:
        "Sorry!":
            pass
    d "It's okay, Author-chan."
    d "We'll just mess around with the settings a bit!"
    call messy