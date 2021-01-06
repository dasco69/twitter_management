#! /usr/bin/python
# -*- coding: utf-8 -*-

import api.auth
import tweepy
import time
 
# on boucle pour suivre les nouveau abonnées dans la limite de 20 et de 40seconde d'interval
for follower in tweepy.Cursor(api.auth.api.followers).items(20):
    follower.follow()
    #on créer un interval de 40sec
    time.sleep(30)
    #on affiche les followers
    print(follower.screen_name)