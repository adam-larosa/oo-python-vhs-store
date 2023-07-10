import ipdb
import random 
import math
import time
from datetime import datetime, timedelta
from faker import Faker
from lib import *

def seeds():
    
    def create_movie_joins( movie, genre_list ):
        for genre in genre_list:
            MovieGenre( movie, genre )

    ####### GENRES ########
    print( "\n✨ creating genres... ✨" )

    action = Genre( "action")
    adaptation = Genre( "adaptation" )
    adventure = Genre( "adventure" )
    animation = Genre( "animation" )
    biography = Genre( "biography" )
    comedy = Genre( "comedy" )
    crime = Genre( "crime" )
    docudrama = Genre( "docudrama" )
    documentary = Genre( "documentary" )
    drama = Genre( "drama" )
    fantasy = Genre( "fantasy" )
    historical_period_drama = Genre( "historical period drama" )
    history = Genre( "history" )
    horror = Genre( "horror" )
    melodrama = Genre( "melodrama" )
    mystery = Genre( "mystery" )
    romance = Genre( "romance" )
    sci_fi = Genre( "sci-fi" )
    sport = Genre( "sport" )
    thriller = Genre( "thriller" )
    war = Genre( "war" )

    ####### MOVIES ########
    print( "✨ creating movies and movie_genres... ✨" )

    the_color_purple = Movie(
        "The Color Purple",
        1985,
        154,
        "Steven Spielberg",
        "Whoopi Goldberg brings Alice Walker’s Pulitzer Prize-winning feminist novel to life as Celie, a Southern woman who suffered abuse over decades. A project brought to a hesitant Steven Spielberg by producer Quincy Jones, the film marks Spielberg’s first female lead.",
        False
    )
    create_movie_joins( the_color_purple, [ adaptation, historical_period_drama, drama ] )

    frida = Movie(
        "Frida",
        2002,
        123,
        "Julie Taymor",
        "'Frida' chronicles the life Frida Kahlo shared unflinchingly and openly with Diego Rivera, as the young couple took the art world by storm. From her complex and enduring relationship with her mentor and husband to her illicit and controversial affair with Leon Trotsky, to her provocative and romantic entanglements with women, Frida Kahlo lived a bold and uncompromising life as a political, artistic, and sexual revolutionary.",
        True
    )
    create_movie_joins(frida, [biography, adaptation, history, drama, romance])

    queen_of_katwe= Movie(
        "Queen of Katwe",
        2016,
        144,
        "Mira Nair",
        "Living in Katwe, a slum in Kampala, Uganda, is a constant struggle for 10-year-old Phiona, her mother Nakku Harriet and younger members of her family. She and her younger brother help their mother sell maize in the market. She also helps care for her baby brother. Her world changes one day when she meets Robert Katende at a missionary program. Katende coaches soccer and teaches children to play chess at a local center. Curious, Phiona approaches and learns the game. She becomes fascinated with it and soon becomes a top player in the group under Katende's guidance.",
        True
    )
    create_movie_joins(queen_of_katwe, [drama, sport, biography])

    perspepolis = Movie(
        "Persepolis",
        2007,
        96,
        "Marjane Satrapi",
        "In 1970s Iran, Marjane 'Marji' Satrapi watches events through her young eyes and her idealistic family of a long dream being fulfilled of the hated Shah's defeat in the Iranian Revolution of 1979. However as Marji grows up, she witnesses first hand how the new Iran, now ruled by Islamic fundamentalists, has become a repressive tyranny on its own. With Marji dangerously refusing to remain silent at this injustice, her parents send her abroad to Vienna to study for a better life. However, this change proves an equally difficult trial with the young woman finding herself in a different culture loaded with abrasive characters and profound disappointments that deeply trouble her. Even when she returns home, Marji finds that both she and homeland have changed too much and the young woman and her loving family must decide where she truly belongs.",
        True
    )
    create_movie_joins(perspepolis, [animation, war, adaptation, history, biography])

    little_women = Movie(
        "Little Women",
        1994,
        118,
        "Gillian Armstrong",
        "Louisa May Alcott's autobiographical account of her life with her three sisters in Concord, Massachusetts in the 1860s. With their father fighting in the American Civil War, sisters Jo, Meg, Amy and Beth are at home with their mother, a very outspoken women for her time. The story tells of how the sisters grow up, find love and find their place in the world.",
        True
    )
    create_movie_joins(little_women, [drama, romance, adaptation, biography])

    little_women_2 = Movie(
        "Little Women",
        2019,
        135,
        "Greta Gerwig",
        "In the years after the Civil War, Jo March (Saoirse Ronan) lives in New York City and makes her living as a writer, while her sister Amy March (Florence Pugh) studies painting in Paris. Amy has a chance encounter with Theodore 'Laurie' Laurence (Timothée Chalamet), a childhood crush who proposed to Jo, but was ultimately rejected. Their oldest sibling, Meg March (Emma Watson), is married to a schoolteacher, while shy sister Beth (Eliza Scanlen) develops a devastating illness that brings the family back together.",
        True
    )
    create_movie_joins(little_women_2, [drama, romance, adaptation, biography])

    thelma_and_louise = Movie(
        "Thelma and Louise",
        1991,
        130,
        "Ridley Scott",
        "Louise is working in a diner as a waitress and has some problems with her boyfriend Jimmy, who, as a musician, is always on the road. Thelma is married to Darryl who likes his wife to stay quiet in the kitchen so that he can watch football on TV. One day they decide to break out of their normal life and jump in the car and hit the road. Their journey, however, turns into a flight when Louise kills a man who threatens to rape Thelma. They decide to go to Mexico, but soon they are hunted by American police.",
        False
    )
    create_movie_joins(thelma_and_louise, [crime, adventure, drama])

    alien = Movie(
        "Alien",
        1979,
        117,  
        "Ridley Scott",
        "Groundbreaking for 1979 science fiction, Sigourney Weaver’s Ellen Ripley is one of the genre’s most iconic female characters. She’s not a damsel—she’s a badass final girl and the only survivor to defeat the monster that mutilated and destroyed every other member of the Nostromo crew.",
        False
    )
    create_movie_joins(alien, [horror, sci_fi])

    mad_max = Movie(
        "Mad Max Fury Road",
        2015,
        140,
        "George Miller",
        "Unearthing feminism in a scorched, hell-on-wheels action flick from road warrior franchise man George Miller isn’t exactly obvious. But though it’s titled after a male character, he is muzzled for much of the film, lending the action to a female imperator and her feminist revolt against the horrors of sexism.",
        False
    )
    create_movie_joins(mad_max, [action, adventure, thriller, sci_fi])

    mustang = Movie(
        "Mustang",
        2015,
        100,
        "Deniz Gamze Ergüven",
        "Early summer. In a village in northern Turkey, Lale and her four sisters are walking home from school, playing innocently with some boys. The immorality of their play sets off a scandal that has unexpected consequences. The family home is progressively transformed into a prison; instruction in homemaking replaces school and marriages start being arranged. The five sisters who share a common passion for freedom, find ways of getting around the constraints imposed on them.",
        True
    )
    create_movie_joins(mustang, [drama])

    girlhood = Movie(
        "Girlhood",
        2014,
        113,
        "Céline Sciamma",
        "Céline Sciamma’s Girlhood, a contemporary narrative with a classic plot that isn’t too distant from anything in the Jane Austen canon, follows a French teenager’s slog through gang life on a quest to self-discovery.",
        True
    )
    create_movie_joins(girlhood, [drama])

    erin = Movie(
        "Erin Brockovich",
        2000,
        113,
        "Steven Soderbergh",
        "Erin Brockovich-Ellis is an unemployed single mother, desperate to find a job, but is having no luck. This losing streak even extends to a failed lawsuit against a doctor in a car accident she was in. With no alternative, she successfully browbeats her lawyer to give her a job in compensation for the loss. While no one takes her seriously, with her trashy clothes and earthy manners, that soon changes when she begins to investigate a suspicious real estate case involving the Pacific Gas & Electric Company. What she discovers is that the company is trying quietly to buy land that was contaminated by hexavalent chromium, a deadly toxic waste that the company is improperly and illegally dumping and, in turn, poisoning the residents in the area. As she digs deeper, Erin finds herself leading point in a series of events that would involve her law firm in one of the biggest class action lawsuits in American history against a multi-billion dollar corporation.",
        False
    )
    create_movie_joins(erin, [drama, biography])

    babadook = Movie(
        "The Babadook",
        2014,
        95,
        "Jennifer Kent",
        "Amelia, who lost her husband in a car crash on the way to give birth to Samuel, their only child, struggles to cope with her fate as a single mom. Samuel's constant fear of monsters and violent reaction to overcome the fear doesn't help her cause either, which makes her friends become distant. When things can not get any worse, they read a strange book in their house about the 'Babadook' monster that hides in the dark areas of their house. Even Amelia seems to feel the effect of Babadook and desperately tries in vain to destroy the book. The nightmarish experiences the two encounter form the rest of the story.",
        True
    )
    create_movie_joins(babadook, [horror, drama, thriller, mystery])

    
    ####### CLIENTS ########
    print( "✨ creating clients... ✨\n" )
    fake = Faker()
    names = set()
    while len( names ) < 20:
        name = fake.name()
        if name not in names:
            names.add( name )
    for name in names:
        client = Client( name, fake.address() )
        print( f"  🍿 {client.name}, welcome to our sick vhs store!" )


    ####### VHS ########
    print( "\n✨ creating vhs... ✨" )
    for i in range( 60 ):
        movies = [ m for m in Movie.all ]
        movie = random.sample( movies, 1 )[0]
        Vhs( movie )

    print( "✨ creating rentals... ✨" )

    def find_vhs_for_rent():
        vhs_tapes = [ v for v in Vhs.all ]
        vhs = random.sample( vhs_tapes, 1 )[0]
        current_rentals = [ r for r in vhs.rentals if r.current == True ]
        not_currently_rented = len( current_rentals ) < 1
        if not_currently_rented:
            return vhs
        return find_vhs_for_rent()    

    for i in range( 20 ):
        number_of_vhs_rented_at_once = random.randint( 1, 3 )
        for j in range( number_of_vhs_rented_at_once ):
            now = datetime.now()
            Rental(
                random.sample( Client.all, 1 )[0],
                find_vhs_for_rent(),
                True,
                now - timedelta( days = random.randint( 1, 5 ) ),
                datetime.now()
            )

    returned_on_date_number = math.ceil( len( Rental.all ) * 0.55 )
    returned_late_number = math.ceil( len( Rental.all ) * 0.15 )
    unreturned_still_late = math.ceil( len( Rental.all ) * 0.1 )

    years = 10
    days_per_year = 365.24
    now = datetime.now()
    opening = now - timedelta( days = ( years * days_per_year ) )

    print( "✨ making some of the rentals be returned on time... ✨" )
    rentals = [ r for r in Rental.all ]
    random.shuffle( rentals ) 

    for returned_on_time in range( returned_on_date_number ):
        opening_in_unix_time = int( time.mktime( opening.timetuple() ) )
        now_in_unix_time = int( time.mktime( now.timetuple() ) )
        rental_unix = random.randint( opening_in_unix_time, now_in_unix_time )
        rental_date = datetime.fromtimestamp( rental_unix )
        return_date = rental_date + timedelta( days = random.randint( 1, 3 ) )
        rental = rentals.pop( random.randrange( len( rentals ) ) )
        rental.current = False
        rental.created_at = rental_date
        rental.updated_at = return_date
        name = rental.client.name
        title = rental.vhs.movie.title
        print( f"  🍿 {name} returned {title} on time." )

    print( f"\n✨ making some of the rentals be returned late... ✨" )
    for returned_late in range( returned_late_number ):
        opening_in_unix_time = int( time.mktime( opening.timetuple() ) )
        now_in_unix_time = int( time.mktime( now.timetuple() ) )
        rental_unix = random.randint( opening_in_unix_time, now_in_unix_time )
        
        rental_date = datetime.fromtimestamp( rental_unix )
        return_date = rental_date + timedelta( days = random.randint( 22, 30 ) )

        rental = rentals.pop( random.randrange( len( rentals ) ) )

        rental.current = False
        rental.created_at = rental_date
        rental.updated_at = return_date
        name = rental.client.name
        title = rental.vhs.movie.title
        print( f"  🍿 {name} was late returning {title}!" )

    print( f"\n✨ making some of the rentals currently past due date... ✨" )
    for returned_late in range( returned_late_number ):
        opening_in_unix_time = int( time.mktime( opening.timetuple() ) )
        now_in_unix_time = int( time.mktime( now.timetuple() ) )
        rental_unix = random.randint( opening_in_unix_time, now_in_unix_time )
        
        rent_at = datetime.fromtimestamp( rental_unix )
        thief_last_seen = rent_at + timedelta( days = random.randint( 37, 75 ) )

        rental = rentals.pop( random.randrange( len( rentals ) ) )
        rental.current = True
        rental.created_at = rent_at
        rental.updated_at = thief_last_seen

        name = rental.client.name
        title = rental.vhs.movie.title
        print( f"  🍿 {name} HAS STOLEN {title}!!!" )


    # creating one last movie with one vhs tape currently rented by one
    # client with that as their only rental.
    print( f"\n✨ making the last client only have one rental... ✨" )
    adam = Client( "Adam", "San Francisco" )
    star = Movie(
        "Star Wars",
        1977,
        121,
        "George Lucas",
        "Amid a galactic civil war, Rebel Alliance spies have stolen plans to the Galactic Empire's Death Star, a massive space station capable of destroying entire planets. Imperial Senator Princess Leia Organa of Alderaan, secretly one of the Rebellion's leaders, has obtained its schematics, but her starship is intercepted by an Imperial Star Destroyer under the command of the ruthless Darth Vader.",
        False
    )
    create_movie_joins( star, [action, adventure, drama, sci_fi, war] )

    now_in_unix_time = int( time.mktime( now.timetuple() ) )
    now_object = datetime.fromtimestamp( now_in_unix_time )
    the_past = now_object - timedelta( days = random.randint( 1, 3 ) )
    return_date = datetime.fromtimestamp( now_in_unix_time ) 
    
    Rental(
        adam,
        Vhs( star ),
        True,
        the_past,
        return_date
    )
    print( f"  🍿 {adam.name} just rented our only copy of {star.title}!" )

    print( "\n\n📼 📼 📼 📼 SEEDED 📼 📼 📼 📼\n" )
