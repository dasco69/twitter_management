#! /usr/bin/python
# coding: utf-8 

import inquirer

def start():
    questions = [
    inquirer.List('reseau',
                    message="Quelles réseau social voulez-vous utilisé?",
                    choices=['Twitter', 'Linkedin'],
                ),
    ]
    answers = inquirer.prompt(questions)

    if answers['reseau'] == 'Twitter':
        twitter()
    if answers['reseau'] == 'Linkedin':
        print('Linkedin')


def twitter():
    questions = [
    inquirer.List('activity',
                    message="Quelles actions voulez vous faire?",
                    choices=['Follow', 'Like', 'Like and Follow', 'Retweet'],
                ),
    ]
    answers = inquirer.prompt(questions)

    if answers['activity'] == 'Follow' : 
        import activity.follow
    if answers['activity'] == 'Like' : 
        questionNbTweet = [
            inquirer.Text('nbTweets',
                        message="Entrer le nombre de tweets") ,
        ]    
        nbTweets = inquirer.prompt(questionNbTweet)

        questionSearch = [
            inquirer.Text('search',
                        message="Quelles categorie de tweet voulais vous chercher?") ,
        ]
        search = inquirer.prompt(questionSearch)

        from activity.like import like
        like(nbTweets['nbTweets'], search['search'])

    if answers['activity'] == 'Like and Follow' : 
        print('Like and Follow')
    if answers['activity'] == 'Retweet' : 
        print('Retweet')


start()
'''
if __name__ == "__main__":
    #import activity.follow
'''