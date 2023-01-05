MovieGenre.destroy_all
Rental.destroy_all
Vhs.destroy_all
Client.destroy_all
Genre.destroy_all
Movie.destroy_all

Faker::UniqueGenerator.clear

def create_movie_joins(movie, genre_array)
    genre_array.each { |genre| MovieGenre.create!(
        movie_id: movie.id, 
        genre_id: genre.id
    )}
end

####### GENRES ########
puts "\n✨ creating genres... ✨"

action = Genre.create(name: "action")
adaptation = Genre.create!(name: "adaptation")
adventure = Genre.create!(name: "adventure")
animation = Genre.create!(name: "animation")
biography = Genre.create!(name: "biography")
comedy = Genre.create!(name: "comedy")
crime = Genre.create!(name: "crime")
docudrama = Genre.create!(name: "docudrama")
documentary = Genre.create!(name: "documentary")
drama = Genre.create!(name: "drama")
fantasy = Genre.create!(name: "fantasy")
historical_period_drama = Genre.create!(name: "historical period drama")
history = Genre.create!(name: "history")
horror = Genre.create!(name: "horror")
melodrama = Genre.create!(name: "melodrama")
mystery = Genre.create!(name: "mystery")
romance = Genre.create!(name: "romance")
sci_fi = Genre.create!(name: "sci-fi")
sport = Genre.create!(name: "sport")
thriller = Genre.create!(name: "thriller")
war = Genre.create!(name: "war")

####### MOVIES ########
puts "✨ creating movies and movie_genres... ✨"

the_color_purple = Movie.create!(
    title: "The Color Purple",
    year: 1985,
    length: 154,
    director: "Steven Spielberg",
    description: "Whoopi Goldberg brings Alice Walker’s Pulitzer Prize-winning feminist novel to life as Celie, a Southern woman who suffered abuse over decades. A project brought to a hesitant Steven Spielberg by producer Quincy Jones, the film marks Spielberg’s first female lead.",
    female_director: false
)
create_movie_joins(the_color_purple, [adaptation, historical_period_drama, drama])

frida = Movie.create!(
            title: "Frida",
            year: 2002,
            length: 123,
            director: "Julie Taymor",
            description: "'Frida' chronicles the life Frida Kahlo shared unflinchingly and openly with Diego Rivera, as the young couple took the art world by storm. From her complex and enduring relationship with her mentor and husband to her illicit and controversial affair with Leon Trotsky, to her provocative and romantic entanglements with women, Frida Kahlo lived a bold and uncompromising life as a political, artistic, and sexual revolutionary.",
            female_director: true
)
create_movie_joins(frida, [biography, adaptation, history, drama, romance])

queen_of_katwe= Movie.create!(
            title: "Queen of Katwe",
            year: 2016,
            length: 144,
            director: "Mira Nair",
            description: "Living in Katwe, a slum in Kampala, Uganda, is a constant struggle for 10-year-old Phiona, her mother Nakku Harriet and younger members of her family. She and her younger brother help their mother sell maize in the market. She also helps care for her baby brother. Her world changes one day when she meets Robert Katende at a missionary program. Katende coaches soccer and teaches children to play chess at a local center. Curious, Phiona approaches and learns the game. She becomes fascinated with it and soon becomes a top player in the group under Katende's guidance.",
            female_director: true
)
create_movie_joins(queen_of_katwe, [drama, sport, biography])

perspepolis = Movie.create!(
            title: "Persepolis",
            year: 2007,
            length: 96,
            director: "Marjane Satrapi",
            description: "In 1970s Iran, Marjane 'Marji' Satrapi watches events through her young eyes and her idealistic family of a long dream being fulfilled of the hated Shah's defeat in the Iranian Revolution of 1979. However as Marji grows up, she witnesses first hand how the new Iran, now ruled by Islamic fundamentalists, has become a repressive tyranny on its own. With Marji dangerously refusing to remain silent at this injustice, her parents send her abroad to Vienna to study for a better life. However, this change proves an equally difficult trial with the young woman finding herself in a different culture loaded with abrasive characters and profound disappointments that deeply trouble her. Even when she returns home, Marji finds that both she and homeland have changed too much and the young woman and her loving family must decide where she truly belongs.",
            female_director: true
)
create_movie_joins(perspepolis, [animation, war, adaptation, history, biography])

little_women = Movie.create!(
            title: "Little Women",
            year: 1994,
            length: 118,
            director: "Gillian Armstrong",
            description: "Louisa May Alcott's autobiographical account of her life with her three sisters in Concord, Massachusetts in the 1860s. With their father fighting in the American Civil War, sisters Jo, Meg, Amy and Beth are at home with their mother, a very outspoken women for her time. The story tells of how the sisters grow up, find love and find their place in the world.",
            female_director: true
)
create_movie_joins(little_women, [drama, romance, adaptation, biography])

little_women_2 = Movie.create!(
    title: "Little Women",
    year: 2019,
    length: 135,
    director: "Greta Gerwig",
    description: "In the years after the Civil War, Jo March (Saoirse Ronan) lives in New York City and makes her living as a writer, while her sister Amy March (Florence Pugh) studies painting in Paris. Amy has a chance encounter with Theodore 'Laurie' Laurence (Timothée Chalamet), a childhood crush who proposed to Jo, but was ultimately rejected. Their oldest sibling, Meg March (Emma Watson), is married to a schoolteacher, while shy sister Beth (Eliza Scanlen) develops a devastating illness that brings the family back together.",
    female_director: true
)
create_movie_joins(little_women_2, [drama, romance, adaptation, biography])

thelma_and_louise = Movie.create!(
            title: "Thelma and Louise",
            year: 1991,
            length: 130,
            director: "Ridley Scott",
            description: "Louise is working in a diner as a waitress and has some problems with her boyfriend Jimmy, who, as a musician, is always on the road. Thelma is married to Darryl who likes his wife to stay quiet in the kitchen so that he can watch football on TV. One day they decide to break out of their normal life and jump in the car and hit the road. Their journey, however, turns into a flight when Louise kills a man who threatens to rape Thelma. They decide to go to Mexico, but soon they are hunted by American police.",
            female_director: false
)
create_movie_joins(thelma_and_louise, [crime, adventure, drama])

alien = Movie.create!(
            title: "Alien",
            year: 1979,
            length: 117,  
            director: "Ridley Scott",
            description: "Groundbreaking for 1979 science fiction, Sigourney Weaver’s Ellen Ripley is one of the genre’s most iconic female characters. She’s not a damsel—she’s a badass final girl and the only survivor to defeat the monster that mutilated and destroyed every other member of the Nostromo crew.",
            female_director: false
)
create_movie_joins(alien, [horror, sci_fi])

mad_max = Movie.create!(
            title: "Mad Max Fury Road",
            year: 2015,
            length: 140,
            director: "George Miller",
            description: "Unearthing feminism in a scorched, hell-on-wheels action flick from road warrior franchise man George Miller isn’t exactly obvious. But though it’s titled after a male character, he is muzzled for much of the film, lending the action to a female imperator and her feminist revolt against the horrors of sexism.",
            female_director: false
)
create_movie_joins(mad_max, [action, adventure, thriller, sci_fi])

mustang = Movie.create!(
            title: "Mustang",
            year: 2015,
            length: 100,
            director: "Deniz Gamze Ergüven",
            description: "Early summer. In a village in northern Turkey, Lale and her four sisters are walking home from school, playing innocently with some boys. The immorality of their play sets off a scandal that has unexpected consequences. The family home is progressively transformed into a prison; instruction in homemaking replaces school and marriages start being arranged. The five sisters who share a common passion for freedom, find ways of getting around the constraints imposed on them.",
            female_director: true
)
create_movie_joins(mustang, [drama])

girlhood = Movie.create!(
            title: "Girlhood",
            year: 2014,
            length: 113,
            director: "Céline Sciamma",
            description: "Céline Sciamma’s Girlhood, a contemporary narrative with a classic plot that isn’t too distant from anything in the Jane Austen canon, follows a French teenager’s slog through gang life on a quest to self-discovery.",
            female_director: true
)
create_movie_joins(girlhood, [drama])

erin = Movie.create!(
            title: "Erin Brockovich",
            year: 2000,
            length: 113,
            director: "Steven Soderbergh",
            description: "Erin Brockovich-Ellis is an unemployed single mother, desperate to find a job, but is having no luck. This losing streak even extends to a failed lawsuit against a doctor in a car accident she was in. With no alternative, she successfully browbeats her lawyer to give her a job in compensation for the loss. While no one takes her seriously, with her trashy clothes and earthy manners, that soon changes when she begins to investigate a suspicious real estate case involving the Pacific Gas & Electric Company. What she discovers is that the company is trying quietly to buy land that was contaminated by hexavalent chromium, a deadly toxic waste that the company is improperly and illegally dumping and, in turn, poisoning the residents in the area. As she digs deeper, Erin finds herself leading point in a series of events that would involve her law firm in one of the biggest class action lawsuits in American history against a multi-billion dollar corporation.",
            female_director: false
)
create_movie_joins(erin, [drama, biography])

babadook = Movie.create!(
            title: "The Babadook",
            year: 2014,
            length: 95,
            director: "Jennifer Kent",
            description: "Amelia, who lost her husband in a car crash on the way to give birth to Samuel, their only child, struggles to cope with her fate as a single mom. Samuel's constant fear of monsters and violent reaction to overcome the fear doesn't help her cause either, which makes her friends become distant. When things can not get any worse, they read a strange book in their house about the 'Babadook' monster that hides in the dark areas of their house. Even Amelia seems to feel the effect of Babadook and desperately tries in vain to destroy the book. The nightmarish experiences the two encounter form the rest of the story.",
            female_director: true
)
create_movie_joins(babadook, [horror, drama, thriller, mystery])

####### CLIENTS ########
puts "✨ creating clients... ✨\n"

20.times do 
    names = [
        -> { Faker::Movies::HitchhikersGuideToTheGalaxy.unique.character }, 
        -> { Faker::TvShows::TwinPeaks.unique.character },
        -> { Faker::TvShows::TheFreshPrinceOfBelAir.unique.character },
        -> { Faker::TvShows::RuPaul.unique.queen },
        -> { Faker::BossaNova.unique.artist },
        -> { Faker::Music::Phish.unique.musician },
        -> { Faker::Ancient.unique.hero },
        -> { Faker::Artist.unique.name },
        -> { Faker::DcComics.unique.hero },
        -> { Faker::DcComics.unique.heroine },
        -> { Faker::DcComics.unique.villain },
        -> { Faker::GreekPhilosophers.unique.name },
        -> { Faker::Books::Dune.unique.character },
        -> { Faker::Movies::Hobbit.unique.character },
        -> { Faker::Movies::LordOfTheRings.unique.character },
        -> { Faker::Games::HeroesOfTheStorm.unique.hero },
        -> { Faker::Movies::Departed.unique.character },
        -> { Faker::Movies::PrincessBride.unique.character },
        -> { Faker::Movies::StarWars.unique.character },
        -> { Faker::TvShows::GameOfThrones.unique.character },
        -> { Faker::TvShows::SiliconValley.unique.character },
        -> { Faker::TvShows::StarTrek.unique.character },
        -> { Faker::TvShows::StarTrek.unique.villain }
    ]
    begin
    name = names.shuffle.sample.call
    rescue Faker::UniqueGenerator::RetryLimitExceeded
    name = Faker::Name.unique.name
    end
    puts "  🍿 #{name}, welcome to our sick vhs store!"
    Client.create!(
        name: name, 
        home_address: Faker::Address.full_address
    )
end

####### VHS ########
puts "\n✨ creating vhs... ✨"

movie_ids = Movie.pluck( :id )
60.times do
    Vhs.create!(movie_id: movie_ids.shuffle.sample )
end

####### Rentals ########
puts "✨ creating rentals... ✨"

def find_vhs_id_for_rent
    vhs = Vhs.find( Vhs.pluck( :id ).shuffle.sample )
    return vhs.id if vhs.rentals.where( current: true ).empty?
    find_vhs_id_for_rent
end

# create rentals (min 20, max 60)
client_ids = Client.pluck( :id )
20.times do
    number_of_vhs_rented_at_once = rand(1..3)
    number_of_vhs_rented_at_once.times do
        Rental.create!(
            client: Client.find( client_ids.shuffle.sample ), 
            vhs_id: find_vhs_id_for_rent,
            current: true,
            created_at: Time.now - rand(1..5).days,
            updated_at: Time.now
        )
    end
end

returned_on_date_number = (Rental.count * 0.55).ceil
returned_late_number = (Rental.count * 0.15).ceil
unreturned_still_late = (Rental.count * 0.1).ceil

# creating an amount of time the store has been open
now = Time.now
opening = now - 10.years

puts "✨ making some of the rentals be returned on time... ✨"
rental_ids = Rental.pluck( :id ).shuffle.shuffle
returned_on_date_number.times do
    rental_date = Time.at rand( opening.to_i..now.to_i )
    returned_date = rental_date + rand( 1..3 ).days
    rental = Rental.find( rental_ids.shift )
    rental.update!(
        current: false,  
        created_at: rental_date, 
        updated_at: returned_date
    )
    name = rental.client.name
    title = rental.vhs.movie.title
    puts "  🍿 #{name} returned #{title} on time."
end

puts "\n✨ making some of the rentals be returned late... ✨"
returned_late_number.times do
    rented = Time.at rand( opening.to_i..now.to_i )
    returned = rented + rand( 21..29 ).days
    rental = Rental.find( rental_ids.shift )
    rental.update!(
        current: false,  
        created_at: rented, 
        updated_at: returned
    )
    name = rental.client.name
    title = rental.vhs.movie.title
    puts "  🍿 #{name} was late returning #{title}!"
end

puts "\n✨ making some of the rentals currently past due date... ✨"
unreturned_still_late.times do
    rented = Time.at rand( opening.to_i..now.to_i )
    customer_last_seen = rented + rand( 37..75 ).days
    rental = Rental.find( rental_ids.shift )
    rental.update!(
        current: true,  
        created_at: rented, 
        updated_at: customer_last_seen
    )
    name = rental.client.name
    title = rental.vhs.movie.title
    puts "  🍿 #{name} HAS STOLEN #{title}!!!"
end


# creating one last movie with one vhs tape currently rented by one
# client with that as their only rental.
puts "\n✨ making the last client only have one rental... ✨"
adam = Client.create!( name: "Adam", home_address: "San Francisco" )
star = Movie.create!(
    title: "Star Wars",
    year: 1977,
    length: 121,
    director: "George Lucas",
    description: "Amid a galactic civil war, Rebel Alliance spies have stolen plans to the Galactic Empire's Death Star, a massive space station capable of destroying entire planets. Imperial Senator Princess Leia Organa of Alderaan, secretly one of the Rebellion's leaders, has obtained its schematics, but her starship is intercepted by an Imperial Star Destroyer under the command of the ruthless Darth Vader.",
    female_director: false
)
create_movie_joins star, [action, adventure, drama, sci_fi, war] 
Rental.create!(
    current: true,
    client: adam,
    vhs: Vhs.create!( movie: star ),
    created_at: Time.now - 5.minutes,
    updated_at: Time.now
)
puts "  🍿 #{adam.name} just rented our only copy of #{star.title}!"


puts "\n\n📼 📼 📼 📼 SEEDED 📼 📼 📼 📼\n"
