//
//  GameList.hpp
//  PA03_draft1
//
//  Created by Kelly Sovacool on 11/10/15.
//  Copyright © 2015 Kelly Sovacool. All rights reserved.
//

#ifndef GameList_hpp
#define GameList_hpp
#include <string>
#include <iostream>
#include <vector>
#include "Game.hpp"
using namespace std;
class GameList {
public:
    GameList();//default constructor
    //~GameList();//destructor
    
    // sort game list by lexicographical order
    void Lex_Sort();
    
    // Insert a new game record into the game list.
    // The game has name gn, number of copies in stock is gc
    // price is gp, and user score is gs
    // Note that the vector of Game objects should be maintained // in the lexicographical order based on the game names.
    // If the game name already exists in the list,
    // then upgrade the record with gc, gp and gs.
    void Insert(string gn, int gc, double gp, double gs);
    
    // check if key is in existing gname
    bool string_match(string key, string gname);
    
    // Search for matched games with the given key of GName
    // A game whose name contains GName will be found
    // If a game is found, print its name, number of copies in stock, // the price and user score
    // otherwise report No Matched Game is in stock.
    void Search(string GName);
    
    // Delete a game record with the name of GName, // If the game is not in the list, do nothing.
    void Delete(string GName);
    
    // Print the game records in stock
    // They are in the lexicographical order based on game names
    void Print();

private:
    int gameCount; // total number of game copies in stock
    vector<Game> glist; // a vector to store Game objects in stock
};
#endif /* GameList_hpp */
