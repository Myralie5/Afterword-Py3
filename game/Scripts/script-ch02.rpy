label ch02_main:
    scene bg club_day
    with dissolve_scene_half
    play music t2
    "Another day passes, and it's time for the club meeting already."
    "I've gotten a little more comfortable here over the past couple days."
    "Entering the clubroom, the usual scene greets me."
    $ writefile("&#80;&#114;&#111;&#98;&#108;&#101;&#109;&#115;&#32;&#65;&#114;&#111;&#115;&#101;&#46;&#46;&#46;")
    show sayori turned happ om ce rup lup at t11 zorder 1
    s "Hey there!"
    mc "Hey."
    mc "Heard from Gwynn yet today?"
    $ sref()
    show sayori nerv awkw om
    s "Yeah..."
    s "About that..."
    s "Gwynn..."
    s "She..."
    s "um..."
    show sayori mk e2b b1a lup rup at t31
    show kotonoha turned uniform happ ce mc lchest rdown at f22 zorder 4
    show nastya turned flus mk at t44 zorder 1
    #kotonoha just kotonohaing
    k "What's upppp?!?"
    "Two girls come barging in, one being obviously dragged by the other."
    show kotonoha turned uniform happ ce mc n1 lchest rdown at t32 zorder 1
    show nastya cross n2 mg e4a b1b at f33 zorder 1
    a "Koto... don't do that..."
    $ k_name = "'Koto'"
    $ sref()
    show sayori turned rup anno awkw om at f31 zorder 1
    show nastya cross n2 me e4a b1b at t33 zorder 1
    s "Please don't barge in like that again."
    show  at f31 zorder 1
    show sayori cm at t33 zorder 1
    return