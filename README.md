# LetsBloom.ai Placement Test Project

I have created this repository to store the assignment for the LetsBloom.ai placement test. The project consists of two tasks.

## Task-1: Crafting a Robust RESTful API for Library System Management

### Repo WalkThrough
- **letbloom** - This is the main project directory which contains the project "letsbloom" and application "api" for the working of the task. Along with this we have the general django dependency files
- **README.md** - The readme file for repository
- **.gitignore** & **LICENSE** - Files for the mainataince and usage guidelines repectively

### Technical Insights

#### Database Configuration
The foundation of this project relies on a PostgreSQL database, meticulously configured on my local machine. The integration of this database into the project structure is orchestrated through the meticulous settings in the `settings.py` file within the project named `lets_bloom`.

#### Architectural Layout
Within the overarching project, denoted as `lets_bloom`, an essential constituent surfaces in the form of the `api` app. Strategically positioned, this app fuels the API functionality. In the `urls.py` file residing within the `lets_bloom` project, a meticulously crafted URL link has been established, redirecting traffic seamlessly to the `api` app. Delving deeper, within the `api` app, the intricacies of URL redirection to `views.py` and the definition of a robust `models.py` file unfold. The latter is instrumental in structuring a model class, precisely delineating the requisite attributes intrinsic to a book, subsequently stored with precision in the database.

To encapsulate the project's coherence, pivotal API methods are housed within `views.py` of the `api` app. This pivotal juncture facilitates seamless integration and operationalization of the API. Furthermore, the integration is fortified through the strategic augmentation of the `settings.py` file, encapsulating the addition of the installed `api` app and judiciously configuring the database settings.


### Deployment Details
To deploy the project Python3 or above is recommended along with django 4.2.6 or greater. The setup follows the genral PostgreSQL version 14 or above. Follow the standard django guidelines with recommended virtualenv installation for best output
