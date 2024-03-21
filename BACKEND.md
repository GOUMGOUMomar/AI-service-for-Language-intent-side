To run the code parfectly you should follow these steps:

1) In your Azur accounte create a new instance of AI service for Language it should be
   'TextAnalytics' type
2) After creating the instance, on the left side look for the section "Keys and Endpoint"
3) In this section you will find KEY 1, KEY 2 and Endpoint, copy one of those keys and the 
   Endpoint and past them in the file 'config.json'
4) In the created service of AI service for Language, on the overview section scroll down
   you will find 'Get started with Language Studio' click on it
5) In the displayed page, you will find the option of Create new, click on it and select the 
   option of conversational language understanding
6) click on cancel for the displayed popup, we will use the easy way lol
7) Click on import and select the file datasets, chose the name if you don't wanna use the default 
   name which is'RecipeAssistant'
8) Get the project name to save it in config.json.
9) You can add more utternaces using GPT model, go to Data labeling click on Suggest utterances,
   and select your GPT model that will generate more utternaces.
10) On the left side, go to Training jobs, chose the standerd option because the dataset is in 
    english, and Azure provides us to train the models that use datasets in english for free.
11) After training the model, go to Deploying a model and chose a name for the deployment, copy 
   the name and save it on the config.json.
12) To test the code, you should just modify the query variable inside pytest file, enjoy!


note: if you wanna use my config.json contact me on omargoumgoum0@gmail.com
 