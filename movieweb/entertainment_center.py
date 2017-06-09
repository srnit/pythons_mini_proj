import media
import fresh_tomatoes
#toy_story=media.Movie();
##toy_story=media.Movie("toy story","a story",
	#"http://upload.wikimedia.org/wikimedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=vwyZH85NQC4")
Bahubali2=media.Movie("Bahubali 2","Story of a warior","bahubali.jpg","https://youtu.be/LEY1F3kKc1Y")
Bank_chor=media.Movie("Bank Chor","commedy","Bank_chor.jpg","https://www.youtube.com/watch?v=Kx0jZWnlS3Y");
Justice_legue=media.Movie("Justice Legue"," justice","justice legue.jpg","https://www.youtube.com/watch?v=3cxixDgHUYw")
movies=[Bahubali2,Bank_chor,Justice_legue];
fresh_tomatoes.open_movies_page(movies);