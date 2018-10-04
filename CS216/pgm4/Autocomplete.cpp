// CS216-002
// Pgm 3
// Kelly Sovacool

#include "Autocomplete.h"
#include <vector>
#include <string>
#include "Term.h"

Autocomplete::Autocomplete(){
	root = NULL;
	count_total = 0;
	count_left = 0;
}

// insert new terms into binary tree, maintaining lexicographic order
// also maintains balanced tree and accurate count of terms
void Autocomplete::insert(Term newterm) {
	count++;
	bool insert_left;
	if (root != NULL) {
		Term current = *root;
		do {
			if (newterm.query < current.query) // if current > newterm
				current = *(current.left);
				count_left++;
				insert_left = true;
			else // current < newterm
				current = *(current.right);
				insert_left = false;
		}  while (current != NULL);
		// current is now position where newterm should be inserted
		if (insert_left)
			current.left = &newterm;
		else
			current.right = &newterm;
		
		// maintain balanced tree
		balance();
	}
	else { // first Term
		root = &newterm;
		newterm.left = NULL;
		newterm.right = NULL;
	}
}

// check whether tree is balanced
// left nodes should be within 1 node of half the total nodes
// assumes count attributes are correct (maintained in insert fcn)
bool Autocomplete::isBalanced() {
	bool ret_val;
	if (count_left-1 < count_total/2 < count_left+1)
		ret_val = true;
	else
		ret_val = false;
	return ret_val;
}

// balance the tree
// fcn only does anything if tree is unbalanced
// since balance check is executed every time new term inserted,
// tree will never be imbalanced by more than 2 nodes
void Autocomplete::balance() {
	if (!isBalanced()) {
		// determine which side is too big
		if (count_left > count_total/2) {// left is too big
			// find rightmost node of root's lefts --> new root
			Term newroot = *((*root).left);
			while (*(newroot.right) != NULL)
				newroot = *(newroot.right);
			newroot.right = root; // root becomes right of new root
			root = &newroot;
			// rearrange lefts of old root
			Term* oldroot = (*root).right;
			rearrange((*oldroot).left);
		}
		else { // right is too big
			// find leftmost node of root's rights --> new root
			Term newroot = *((*root).right);
			while (*(newroot.left) != NULL)
				newroot = *(newroot.left);
			newroot.left = root; // root becomes left of new root
			root = &newroot;
			// rearrange rights of old root
			Term* oldroot = (*root).left;
			rearrange((*oldroot).right);
		}
		// make sure balance executed correctly
		string statement;
		if (isBalanced())
			statement = "Tree balanced.";
		else
			statement = "Warning: tree still imbalanced after attempt to balance it!";
		cout << statement << endl;
	}
}
// postorder traversal of branch
// rearranging nodes to make a balanced tree
void rearrange(Term* node) {
	if (node != NULL) {
		rearrange((*node).left);
		rearrange((*node).right);
		// process node
		Term* current = root;
		bool insert_left;
		do {
			if ((*node).query < (*current).query) // if current > node
				current = (*current).left;
				count_left++;
				insert_left = true;
			else // current < node
				current = (*current).right;
				insert_left = false;
		}  while (current != NULL);
			// current is now position where term should be reinserted
		if (insert_left)
			(*current).left = node;
		else
			(*current).right = node;
	}
}	

Term* allMatches(string prefix) {
	Term* matches = new Terms[0]; // array to return
}
