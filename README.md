# Movie_Recommendation_System

## Abstract
A recommendation system analyses the browsing history and user preferences and provides suggestions through a filtering technique. A movie recommendation system, or a movie recommender system, is a Machine Learning approach to predicting the users’ film preferences based on their previous choices and behaviour. Content based Movie Recommendation System using Feature Extraction (CMRSFE) an advanced filtration technique that predicts the possible movie choices based on the user concerns and preferences towards a domain-specific item. In this work, the model mines the movie datasets to extract all the important information, such as, popularity, genres, keywords, overview, cast and crew, necessary for recommendation. The “TMDB-The Movie Database” dataset is made use of, to create the machine learning model for the recommendation system. Finally, the model recommends the top movies as a recommendation to the user.

## Problem Definition
The user enters a movie name present in the dataset as the input. The model extract features such as movie_id, title, genre, keywords, overview, cast, crew from the dataset and provides recommendation of the top similar movies as the output.

## Working Mechanism
The project at hand is an intricate movie recommendation system that adeptly utilizes the TMDB (The Movie Database) dataset. Comprising a well-structured series of modules, the system meticulously processes data, extracts relevant information, and ultimately crafts an interactive recommendation platform. This endeavor aims to provide users with a seamlessly engaging experience, marrying textual analysis with visual representation through the inclusion of movie posters.

1. **Data Preprocessing:** At the project's outset, the TMDB dataset undergoes a meticulous cleaning process to ensure data quality. Null values and duplicate entries are methodically eliminated, laying the foundation for a reliable dataset. To further streamline subsequent analyses, attributes within the dataset are transformed into lists of strings. This transformation is facilitated by the ast.literal_eval() library, proving essential for later stages when specific attributes like 'genres,' 'keywords,' 'cast,' and 'crew' need to be accessed and processed.
2. **Content Extraction:** User-defined functions take center stage in this phase, systematically extracting essential attributes that form the backbone of the movie representation. Key features, including 'movie_id,' 'title,' 'genre,' 'keyword,' 'overview,' 'cast,' and 'crew,' are meticulously isolated. These attributes, collectively forming a comprehensive representation of each movie, serve as the building blocks for subsequent analyses and recommendation generation.
3. **Text Vectorization:** The 'tags' column emerges as a pivotal component, created by amalgamating relevant textual attributes such as 'genre,' 'keyword,' 'overview,' 'cast,' and 'crew.' The 'tags' column undergoes a transformative process through vectorization, employing the Bag of Words technique. Leveraging the CountVectorizer from the sklearn.feature_extraction.text library, this step ensures the conversion of textual information into numerical vectors. Setting max_features to 5000 optimizes efficiency, focusing on the most impactful terms. Simultaneously, the removal of common stop words enhances the significance of the retained terms.
4. **Distance Calculation Module:** The Distance Calculation Module plays a pivotal role in refining the recommendation system, introducing the Cosine Similarity technique as the primary measure to quantify the distance between movie vectors. This step enhances the precision of recommendations by considering the angle between vectors, represented by the 'tags' column.
The Cosine Similarity formula, 
cosθ = □((u.v)/|(|u|)||(|v|)|cosθ)
, is employed to determine the cosine of the angle between two vectors, 'u' and 'v,' where 'u' and 'v' represent the vectorized 'tags' of two distinct movies. This mathematical formulation assesses the similarity between movies based on their textual content, producing a value between -1 (indicating perfect dissimilarity) and 1 (indicating perfect similarity), with 0 denoting orthogonality.
The cosine_similarity() function is instrumental in executing this calculation, providing a quantitative measure of the cosine similarity between movie vectors. This calculation establishes the foundation for discerning the distance or similarity between movies grounded in their textual features.
The subsequent utilization of the enumerate() function in tandem with cosine similarity enables the enumeration of movie indices along with their associated cosine similarity scores. This enumeration proves crucial in the ranking of movies, facilitating the identification of the top similar movies based on their textual content. This refined ranking is fundamental to the recommendation process, ensuring that users receive suggestions with the least textual distance, thereby enhancing the relevance and accuracy of movie recommendations.
5. **Recommendation System:** The heart of the project lies in the recommendation system, anchored by the 'recommend' function. This user-defined function employs cosine similarity to calculate distances between movies based on their vectorized 'tags.' The enumerate function then comes into play, facilitating the ranking and recommendation of the top movies when the function is called with a specific movie title. This recommendation system is the linchpin, delivering personalized suggestions grounded in content similarity and catering to users' individual preferences.
6. **Integration of Movie Posters:** To elevate the visual appeal of the recommendation system, movie posters are dynamically sourced through an API from api.themoviedb.org. The Streamlit library proves invaluable in seamlessly linking these posters with their corresponding movie indices. This integration introduces a visually rich dimension to the recommendation system, allowing users not only to peruse textual recommendations but also to visually explore the suggested movies through their associated posters.
7. **User Interaction:** The user interacts with the system by invoking the 'recommend' function with a specific movie title. This interactive process results in the function returning a list of the top similar movies, accompanied by their associated posters. Users are thus empowered to explore recommendations tailored to their unique preferences and interests.
8. **Enhanced User Experience:** The crux of the project lies in the amalgamation of textual analysis and visual representation, significantly elevating the user experience. Users can make informed decisions by considering both content-based similarities and the visual allure presented by movie posters. The Streamlit interface functions as an intuitive and user-friendly platform, enabling users to seamlessly explore and select recommended movies.

## Software Requirements
1.	**Programming Language:**
	- Python: The project is implemented in Python, so ensure Python is installed.
2.	**Development Environment:**
	- Integrated Development Environment (IDE): Use a Python-compatible IDE like PyCharm, Jupyter Notebook, or VSCode for coding convenience.
3.	**Libraries and Packages:**
	- Pandas: For data manipulation and analysis.
	- NumPy: For numerical operations on data.
	- Scikit-learn: For implementing machine learning algorithms and tools.
	- Ast: For literal evaluation of strings to Python expressions.
	- Streamlit: For creating interactive web applications.
	- Requests: For making HTTP requests to APIs.
	- Pickle: Serialization and deserialization of Python objects. It's used to save and load Python objects in a binary format.
4.	**Text Vectorization Library:**
	- Scikit-learn's CountVectorizer or any other text vectorization library for transforming textual data.
5.	**API Key:**
	- Obtain an API key for accessing external data, such as movie posters from themoviedb.org.
6.	Web Browser:
	- A web browser to interact with the Streamlit web application.
7.	**Movie Database:**
	- The datasets files.

## Result
![image](https://github.com/sairaj0003/Movie_Recommendation_System/assets/140234339/1c5399c6-ac78-43bc-b1b8-e6c76bd09a64)

## Conclusion
In conclusion, the movie recommendation system represents a comprehensive integration of advanced data processing techniques and user-centric design principles. The project, spanning multiple modules and methodologies, creates a robust platform for users to explore and discover movies based on both textual content and visual appeal. The interplay between data preprocessing, content extraction, text vectorization, distance calculation, recommendation generation, and poster integration results in a cohesive and engaging system. The meticulous orchestration of these elements, combined with a thoughtful application flow, positions the recommendation system as a noteworthy example of the synergy between technology and user experience in the realm of movie recommendations.
