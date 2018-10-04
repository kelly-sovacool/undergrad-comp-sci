//
//  GameList.cpp
//  PA03_draft1
//
//  Created by Kelly Sovacool on 11/10/15.
//  Copyright © 2015 Kelly Sovacool. All rights reserved.
//
#include <vector>
#include <algorithm>
#include <iostream>
#include "GameList.hpp"
#include "Game.hpp"

GameList::GameList() {
    int gameCount = 0;
    vector<Game> glist;
}

// sort game list by lexicographical order
void GameList::Lex_Sort() {
    for (int j=0; j<glist.size(); j++) {
        // for each game
        for (int k=0; k<(glist.size()-1); k++) {
            // if this game should be after next game
            if (glist[k].name > glist[k+1].name) {
                // swap
                Game copy = glist[k];
                glist[k] = glist[k+1];
                glist[k+1] = copy;
            }
        }
    }
}

// Insert a new game record into the game list.
// The game has name gn, number of copies in stock is gc
// price is gp, and user score is gs
// Note that the vector of Game objects should be maintained
// in the lexicographical order based on the game names.
// If the game name already exists in the list,
// then upgrade the record with gc, gp and gs.
void GameList::Insert(string gn, int gc, double gp, double gs) {
    int i = 0;
    bool inList = false;
    while (i<glist.size() && !inList) {
        if (gn == glist[i].name) { // update existing game
            glist[i].count = gc;
            glist[i].price = gp;
            glist[i].score = gs;
            inList = true;
        }
        i++;
    }
    if (!inList) { // insert new game
        glist.push_back(Game(gn, gc, gp, gs));
        gameCount += gc;
        // sort in lexicographical order
        Lex_Sort();
    }
}

// check if key is in existing gname
bool GameList::string_match(string key , string gname) {
    bool doesMatch = false;
    int i = 0;
    while(i<gname.length() && !doesMatch) {
        if (gname.substr(i, key.length()) == key)
            doesMatch = true;
        i++;
    }
    return doesMatch;
}

// Search for matched games with the given key of GName
// A game whose name contains GName will be found
// If a game is found, print its name, number of copies in stock,
// the price and user score
// otherwise report No Matched Game is in stock.
void GameList::Search(string GName){
    bool isFound = false;
    int i=0;
    while (i<glist.size() && !isFound) {
        // if GName matches existing game name
        if (string_match(GName, glist[i].name)) {
            cout << "Name: "<< glist[i].name << endl;
            cout << "Copies in stock: " << glist[i].count << endl;
            cout << "Price: $" << glist[i].price << endl;
            cout << "Score: " << glist[i].score << endl;
            isFound = true;
        }
        i++;
    }
    if (!isFound)
        cout << "No matched game is in stock." << endl;
}

// Delete a game record with the name of GName,
// If the game is not in the list, do nothing.
void GameList::Delete(string GName){
    int i=0;
    bool notDone = true;
    while(i<glist.size() && notDone) {
        if (GName == glist[i].name) {
            gameCount -= glist[i].count;
            // swap this game and last game
            Game copy = glist[glist.size()-1];
            glist[glist.size()-1] = glist[i];
            glist[i] = copy;
            // remove game
            glist.pop_back();
            // sort
            Lex_Sort();
            notDone = false;
        }
        i++;
    }
    if (notDone)
        cout << GName << " is not in the list. Deletion failed." << endl;
}
// Print the game records in stock
// They are in the lexicographical order based on game names
void GameList::Print(){
    cout << "--- Total: " << gameCount << " copies of games in stock ---" << endl;
    for (int i=0; i<glist.size(); i++) {
        cout << "Name: "<< glist[i].name << endl;
        cout << "   Count: "<< glist[i].count << endl;
        cout << "   Price: $"<< glist[i].price << endl;
        cout << "   Score: "<< glist[i].score << endl;
    }
    cout << "-------------------------------------------" << endl;
}