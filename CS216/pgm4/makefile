OBJECTS = main.o Term.o Autocomplete.o
HEADERS = Term.h Autocomplete.h
CS216PA4: $(OBJECTS)
	g++ $^ -o CS216PA4
%.o: %.cpp $(HEADERS)
	g++ -c $< -o $@
clean:
	rm -i *.o CS216PA4
