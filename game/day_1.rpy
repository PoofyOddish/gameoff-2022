label day_1:
    scene bg house

    y "What a beautiful Saturday morning! I can't wait to get cooking with Mark."

    show mark happy

    m "Took you long enough to get here! Let's get inside and get cooking!"

    scene bg kitchen

    show mark happy at left

    y "What are we cooking today?"

    m "Well, since blueberries are in season, I figured we would make some blueberry muffins. Doesn't that sound great?"

    y "It sure does! How can I help?"

    m "I knew you'd like it! Can you go grab some flour and sugar from the pantry?"

    y "I think I can handle that!"

    scene bg pantry

    y "What did I need to grab again..."

    default ingredient = ""
    default chances = 3
    default flourFound = False
    default sugarFound = False

menu get_ingredients:

    "Black Pepper":
        $ ingredient = 'black pepper'
        $ chances -= 1
        jump wrong

    "Flour" if flourFound == False:
        $ ingredient = 'flour'
        $ flourFound = True
        jump right

    "Corn Flakes":
        $ ingredient = 'cereal'
        $ chances -= 1
        jump wrong

    "Broom":
        $ ingredient = 'broom'
        $ chances -= 1
        jump wrong

    "Sugar" if sugarFound == False:
        $ ingredient = 'sugar'
        $ sugarFound = True
        jump right

    
    "Barlett Pears":
        $ ingredient = 'pears'
        $ chances -= 1
        jump wrong

label wrong:

    scene bg kitchen

    y "Got what you asked for! Here's the [ingredient]."

    show mark happy
    
    if chances == 0:

        m "You've got to be kidding me. Get out. I'm tired of your nonsense."

        y "Why are you taking this so seriously? I was just kidding around..."

        m "You don't get it. You'll never get it. Leave."

        y "Fine."

        ".:. Goofy Goober Ending."

        return

    else:

        if not sugarFound and not flourFound:

            m "*laughs* You goober. We still need the flour and sugar. Try again!"

        elif not sugarFound:

            m "*laughs* You goober. We still need the sugar. Try again!"

        else:

            m "*laughs* You goober. We still need the flour. Try again!"

        scene bg pantry

        y "What did I need to grab again..."
        
        jump get_ingredients

label right:

    scene bg kitchen

    y "Got what you asked for! Here's the [ingredient]."

    if sugarFound and flourFound:
        
        jump cooking_muffins

    elif sugarFound:
        
        show mark happy

        m "Great work! Now just go grab the flour and we can get started!"

    else:

        show mark happy

        m "Great work! Now just go grab the sugar and we can get started!"

    scene bg pantry

    y "What did I need to grab again..."
    
    jump get_ingredients


label cooking_muffins:
    
    scene bg kitchen
    show mark happy at left
    with dissolve

    m "We've got all of our ingredients! Let's get cooking!"

    scene bg muffins

    y "Woooow!~ They look so good! Can we dig in?"

    scene bg kitchen
    show mark happy
    with dissolve

    m "Absolutely. They're hot though, so be careful!"

    "You and Mark dig into the muffins. They're delicious!"

    jump end_day_1

label end_day_1:

    scene bg house
    show mark happy at right

    y "Thanks so much for having me over today!"

    m "Thank {b}you{/b} for helping me cook! Will you be able to come over again next Saturday for another cooking lesson?"

    y "You know it! See you then!"

    "You headed back to your house, stomach full of delicious blueberry muffins."


    # This ends the game.

    return