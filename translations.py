#!/usr/bin/python
# coding=utf-8
translations = {
"A boy drinks .":"Ein Junge trinkt",
"A boy drinks milk .":"Ein Junge trinkt Milch",
"A boy drinks the milk .":"Ein Junge trinkt die Milch",
"A boy drinks the water .":"Ein Junge trinkt das Wasser",
"A boy drinks water .":"Ein Junge trinkt Wasser",
"A boy eats .":"Ein Junge isst",
"A boy eats an apple .":"Ein Junge isst einen Apfel",
"A boy eats bread .":"Ein Junge isst Brot",
"A boy eats the apple .":"Ein Junge isst den Apfel",
"A boy eats the bread .":"Ein Junge isst das Brot",
"A boy is a child .":"Ein Junge ist ein Kind",
"A boy is drinking .":"Ein Junge trinkt",
"A boy is drinking milk .":"Ein Junge trinkt Milch",
"A boy is drinking the milk .":"Ein Junge trinkt die Milch",
"A boy is drinking the water .":"Ein Junge trinkt das Wasser",
"A boy is drinking water .":"Ein Junge trinkt Wasser",
"A boy is eating .":"Ein Junge isst",
"A boy is eating an apple .":"Ein Junge isst einen Apfel",
"A boy is eating bread .":"Ein Junge isst Brot",
"A boy is eating the apple .":"Ein Junge isst den Apfel",
"A boy is eating the bread .":"Ein Junge isst das Brot",
"A boy":"Ein Junge",
"A child drinks .":"Ein Kind trinkt",
"A child drinks milk .":"Ein Kind trinkt Milch",
"A child drinks the milk .":"Ein Kind trinkt die Milch",
"A child drinks the water .":"Ein Kind trinkt das Wasser",
"A child drinks water .":"Ein Kind trinkt Wasser",
"A child eats .":"Ein Kind isst",
"A child eats an apple .":"Ein Kind isst einen Apfel",
"A child eats bread .":"Ein Kind isst Brot",
"A child eats the apple .":"Ein Kind isst den Apfel",
"A child eats the bread .":"Ein Kind isst das Brot",
"A child is drinking .":"Ein Kind trinkt",
"A child is drinking milk .":"Ein Kind trinkt Milch",
"A child is drinking the milk .":"Ein Kind trinkt die Milch",
"A child is drinking the water .":"Ein Kind trinkt das Wasser",
"A child is drinking water .":"Ein Kind trinkt Wasser",
"A child is eating .":"Ein Kind isst",
"A child is eating an apple .":"Ein Kind isst einen Apfel",
"A child is eating bread .":"Ein Kind isst Brot",
"A child is eating the apple .":"Ein Kind isst den Apfel",
"A child is eating the bread .":"Ein Kind isst das Brot",
"A child":"Ein Kind",
"A girl drinks .":"Ein Madchen trinkt",
"A girl drinks milk .":"Ein Madchen trinkt Milch",
"A girl drinks the milk .":"Ein Madchen trinkt die Milch",
"A girl drinks the water .":"Ein Madchen trinkt das Wasser",
"A girl drinks water .":"Ein Madchen trinkt Wasser",
"A girl eats .":"Ein Madchen isst",
"A girl eats an apple .":"Ein Madchen isst einen Apfel",
"A girl eats bread .":"Ein Madchen isst Brot",
"A girl eats the apple .":"Ein Madchen isst den Apfel",
"A girl eats the bread .":"Ein Madchen isst das Brot",
"A girl is a child .":"Ein Madchen ist ein Kind",
"A girl is drinking .":"Ein Madchen trinkt",
"A girl is drinking milk .":"Ein Madchen trinkt Milch",
"A girl is drinking the milk .":"Ein Madchen trinkt die Milch",
"A girl is drinking the water .":"Ein Madchen trinkt das Wasser",
"A girl is drinking water .":"Ein Madchen trinkt Wasser",
"A girl is eating .":"Ein Madchen isst",
"A girl is eating an apple .":"Ein Madchen isst einen Apfel",
"A girl is eating bread .":"Ein Madchen isst Brot",
"A girl is eating the apple .":"Ein Madchen isst den Apfel",
"A girl is eating the bread .":"Ein Madchen isst das Brot",
"A girl":"Ein Madchen",
"A man drinks .":"Ein Mann trinkt",
"A man drinks milk .":"Ein Mann trinkt Milch",
"A man drinks the milk .":"Ein Mann trinkt die Milch",
"A man drinks the water .":"Ein Mann trinkt das Wasser",
"A man drinks water .":"Ein Mann trinkt Wasser",
"A man eats .":"Ein Mann isst",
"A man eats an apple .":"Ein Mann isst einen Apfel",
"A man eats bread .":"Ein Mann isst Brot",
"A man eats the apple .":"Ein Mann isst den Apfel",
"A man eats the bread .":"Ein Mann isst das Brot",
"A man is drinking .":"Ein Mann trinkt",
"A man is drinking milk .":"Ein Mann trinkt Milch",
"A man is drinking the milk .":"Ein Mann trinkt die Milch",
"A man is drinking the water .":"Ein Mann trinkt das Wasser",
"A man is drinking water .":"Ein Mann trinkt Wasser",
"A man is eating .":"Ein Mann isst",
"A man is eating an apple .":"Ein Mann isst einen Apfel",
"A man is eating bread .":"Ein Mann isst Brot",
"A man is eating the apple .":"Ein Mann isst den Apfel",
"A man is eating the bread .":"Ein Mann isst das Brot",
"A man":"Ein Mann",
"A woman drinks .":"Eine Frau trinkt",
"A woman drinks milk .":"Eine Frau trinkt Milch",
"A woman drinks the milk .":"Eine Frau trinkt die Milch",
"A woman drinks the water .":"Eine Frau trinkt das Wasser",
"A woman drinks water .":"Eine Frau trinkt Wasser",
"A woman eats .":"Eine Frau isst",
"A woman eats an apple .":"Eine Frau isst einen Apfel",
"A woman eats bread .":"Eine Frau isst Brot",
"A woman eats the apple .":"Eine Frau isst den Apfel",
"A woman eats the bread .":"Eine Frau isst das Brot",
"A woman is drinking .":"Eine Frau trinkt",
"A woman is drinking milk .":"Eine Frau trinkt Milch",
"A woman is drinking the milk .":"Eine Frau trinkt die Milch",
"A woman is drinking the water .":"Eine Frau trinkt das Wasser",
"A woman is drinking water .":"Eine Frau trinkt Wasser",
"A woman is eating .":"Eine Frau isst",
"A woman is eating an apple .":"Eine Frau isst einen Apfel",
"A woman is eating bread .":"Eine Frau isst Brot",
"A woman is eating the apple .":"Eine Frau isst den Apfel",
"A woman is eating the bread .":"Eine Frau isst das Brot",
"A woman":"Eine Frau",
"Das Brot ist gut .":"The bread is good",
"Das Junge isst Brot .":"The boy eats bread",
"Das Junge isst das Brot .":"The boy eats the bread",
"Das Kind isst .":"The child eats",
"Das Kind isst Brot .":"The child eats bread",
"Das Kind isst das Brot .":"The child eats the bread",
"Das Kind isst den Apfel .":"The child eats the apple",
"Das Kind isst einen Apfel .":"The child eats an apple",
"Das Kind ist ein Junge .":"The child is a boy",
"Das Kind trinkt .":"The child drinks",
"Das Kind trinkt das Wasser .":"The child drinks the water",
"Das Kind trinkt die Milch .":"The child drinks the milk",
"Das Kind trinkt Milch .":"The child drinks milk",
"Das Kind trinkt Wasser .":"The child drinks water",
"Das Kind":"The child",
"Das Mädchen isst .":"The girl eats",
"Das Mädchen isst Brot .":"The girl eats bread",
"Das Mädchen isst das Brot .":"The girl eats the bread",
"Das Mädchen isst den Apfel .":"The girl eats the apple",
"Das Mädchen isst einen Apfel .":"The girl eats an apple",
"Das Mädchen ist ein Kind .":"The girl is a child",
"Das Mädchen trinkt .":"The girl drinks",
"Das Mädchen trinkt das Wasser .":"The girl drinks the water",
"Das Mädchen trinkt die Milch .":"The girl drinks the milk",
"Das Mädchen trinkt Milch .":"The girl drinks milk",
"Das Mädchen trinkt Wasser .":"The girl drinks water",
"Das Mädchen":"The girl",
"Der Junge isst .":"The boy eats",
"Der Junge isst Brot .":"The boy eats bread",
"Der Junge isst das Brot .":"The boy eats the bread",
"Der Junge isst den Apfel .":"The boy eats the apple",
"Der Junge isst einen Apfel .":"The boy eats an apple",
"Der Junge ist ein Kind .":"The boy is a child",
"Der Junge trinkt .":"The boy drinks",
"Der Junge trinkt das Wasser .":"The boy drinks the water",
"Der Junge trinkt die Milch .":"The boy drinks the milk",
"Der Junge trinkt Milch .":"The boy drinks milk",
"Der Junge trinkt Wasser .":"The boy drinks water",
"Der Junge":"The boy",
"Der Mann isst .":"The man eats",
"Der Mann isst Brot .":"The man eats bread",
"Der Mann isst das Brot .":"The man eats the bread",
"Der Mann isst den Apfel .":"The man eats the apple",
"Der Mann isst einen Apfel .":"The man eats an apple",
"Der Mann trinkt .":"The man drinks",
"Der Mann trinkt das Wasser .":"The man drinks the water",
"Der Mann trinkt die Milch .":"The man drinks the milk",
"Der Mann trinkt Milch .":"The man drinks milk",
"Der Mann trinkt Wasser .":"The man drinks water",
"Der Mann":"The man",
"Die Frau isst .":"The woman eats",
"Die Frau isst Brot .":"The woman eats bread",
"Die Frau isst das Brot .":"The woman eats the bread",
"Die Frau isst den Apfel .":"The woman eats the apple",
"Die Frau isst einen Apfel .":"The woman eats an apple",
"Die Frau trinkt .":"The woman drinks",
"Die Frau trinkt das Wasser .":"The woman drinks the water",
"Die Frau trinkt die Milch .":"The woman drinks the milk",
"Die Frau trinkt Milch .":"The woman drinks milk",
"Die Frau trinkt Wasser .":"The woman drinks water",
"Die Frau":"The woman",
"Die Milch ist gut .":"The milk is good",
"Du bist ein Junge .":"You are a boy",
"Du bist ein Kind .":"You are a child",
"Du bist ein Mann .":"You are a man",
"Du bist ein Mädchen .":"You are a girl",
"Du bist eine Frau .":"You are a woman",
"Du isst .":"You eat",
"Du isst Brot .":"You eat bread",
"Du isst das Brot .":"You eat the bread",
"Du isst den Apfel .":"You eat the apple",
"Du isst einen Apfel .":"You eat an apple",
"Du trinkst .":"You drink",
"Du trinkst das Wasser .":"You drink the water",
"Du trinkst die Milch .":"You drink the milk",
"Du trinkst Milch .":"You drink milk",
"Du trinkst Wasser .":"You drink water",
"Ein Junge isst .":"A boy eats",
"Ein Junge isst Brot .":"A boy eats bread",
"Ein Junge isst das Brot .":"A boy eats the bread",
"Ein Junge isst den Apfel .":"A boy eats the apple",
"Ein Junge isst einen Apfel .":"A boy eats an apple",
"Ein Junge ist ein Kind .":"A child is a boy",
"Ein Junge trinkt .":"A boy drinks",
"Ein Junge trinkt das Wasser .":"A boy drinks the water",
"Ein Junge trinkt die Milch .":"A boy drinks the milk",
"Ein Junge trinkt Milch .":"A boy drinks milk",
"Ein Junge trinkt Wasser .":"A boy drinks water",
"Ein Junge":"A boy",
"Ein Kind isst .":"A child eats",
"Ein Kind isst Brot .":"A child eats bread",
"Ein Kind isst das Brot .":"A child eats the bread",
"Ein Kind isst den Apfel .":"A child eats the apple",
"Ein Kind isst einen Apfel .":"A child eats an apple",
"Ein Kind ist ein Junge .":"A child is a boy",
"Ein Kind trinkt .":"A child drinks",
"Ein Kind trinkt das Wasser .":"A child drinks the water",
"Ein Kind trinkt die Milch .":"A child drinks the milk",
"Ein Kind trinkt Milch .":"A child drinks milk",
"Ein Kind trinkt Wasser .":"A child drinks water",
"Ein Kind":"A child",
"Ein Mann isst .":"A man eats",
"Ein Mann isst Brot .":"A man eats bread",
"Ein Mann isst das Brot .":"A man eats the bread",
"Ein Mann isst den Apfel .":"A man eats the apple",
"Ein Mann isst einen Apfel .":"A man eats an apple",
"Ein Mann trinkt .":"A man drinks",
"Ein Mann trinkt das Wasser .":"A man drinks the water",
"Ein Mann trinkt die Milch .":"A man drinks the milk",
"Ein Mann trinkt Milch .":"A man drinks milk",
"Ein Mann trinkt Wasser .":"A man drinks water",
"Ein Mann":"A man",
"Ein Mädchen isst .":"A girl eats",
"Ein Mädchen isst Brot .":"A girl eats bread",
"Ein Mädchen isst das Brot .":"A girl eats the bread",
"Ein Mädchen isst den Apfel .":"A girl eats the apple",
"Ein Mädchen isst einen Apfel .":"A girl eats an apple",
"Ein Mädchen ist ein Kind .":"A girl is a child",
"Ein Mädchen trinkt .":"A girl drinks",
"Ein Mädchen trinkt das Wasser .":"A girl drinks the water",
"Ein Mädchen trinkt die Milch .":"A girl drinks the milk",
"Ein Mädchen trinkt Milch .":"A girl drinks milk",
"Ein Mädchen trinkt Wasser .":"A girl drinks water",
"Ein Mädchen":"A girl",
"Eine Frau isst .":"A woman eats",
"Eine Frau isst Brot .":"A woman eats bread",
"Eine Frau isst das Brot .":"A woman eats the bread",
"Eine Frau isst den Apfel .":"A woman eats the apple",
"Eine Frau isst einen Apfel .":"A woman eats an apple",
"Eine Frau trinkt .":"A woman drinks",
"Eine Frau trinkt das Wasser .":"A woman drinks the water",
"Eine Frau trinkt die Milch .":"A woman drinks the milk",
"Eine Frau trinkt Milch .":"A woman drinks milk",
"Eine Frau trinkt Wasser .":"A woman drinks water",
"Eine Frau":"A woman",
"Er isst .":"He eats",
"Er isst Brot .":"He eats bread",
"Er isst das Brot .":"He eats the bread",
"Er isst den Apfel .":"He eats the apple",
"Er isst einen Apfel .":"He eats an apple",
"Er ist ein Junge .":"He is a boy",
"Er ist ein Kind .":"He is a child",
"Er ist ein Mann .":"He is a man",
"Er trinkt .":"He drinks",
"Er trinkt das Wasser .":"He drinks the water",
"Er trinkt die Milch .":"He drinks the milk",
"Er trinkt Milch .":"He drinks milk",
"Er trinkt Wasser .":"He drinks water",
"He drinks .":"Er trinkt",
"He drinks milk .":"Er trinkt Milch",
"He drinks the milk .":"Er trinkt die Milch",
"He drinks the water .":"Er trinkt das Wasser",
"He drinks water .":"Er trinkt Wasser",
"He eats .":"Er isst",
"He eats an apple .":"Er isst einen Apfel",
"He eats bread .":"Er isst Brot",
"He eats the apple .":"Er isst den Apfel",
"He eats the bread .":"Er isst das Brot",
"He is a boy .":"Er ist ein Junge",
"He is a child .":"Er ist ein Kind",
"He is a man .":"Er ist ein Mann",
"He is drinking .":"Er trinkt",
"He is drinking milk .":"Er trinkt Milch",
"He is drinking the milk .":"Er trinkt die Milch",
"He is drinking the water .":"Er trinkt das Wasser",
"He is drinking water .":"Er trinkt Wasser",
"He is eating .":"Er isst",
"He is eating an apple .":"Er isst einen Apfel",
"He is eating bread .":"Er isst Brot",
"He is eating the apple .":"Er isst den Apfel",
"He is eating the bread .":"Er isst das Brot",
"I am a boy .":"Ich bin ein Junge",
"I am a child .":"Ich bin ein Kind",
"I am a girl .":"Ich bin ein Madchen",
"I am a man .":"Ich bin ein Mann",
"I am a woman .":"Ich bin eine Frau",
"I am drinking .":"Ich trinke",
"I am drinking milk .":"Ich trinke Milch",
"I am drinking the milk .":"Ich trinke die Milch",
"I am drinking the water .":"Ich trinke das Wasser",
"I am drinking water .":"Ich trinke Wasser",
"I am eating .":"Ich esse",
"I am eating an apple .":"Ich esse einen Apfel",
"I am eating bread .":"Ich esse Brot",
"I am eating the apple .":"Ich esse den Apfel",
"I am eating the bread .":"Ich esse das Brot",
"I drink .":"Ich trinke",
"I drink milk .":"Ich trinke Milch",
"I drink the milk .":"Ich trinke die Milch",
"I drink the water .":"Ich trinke das Wasser",
"I drink water .":"Ich trinke Wasser",
"I eat .":"Ich esse",
"I eat an apple .":"Ich esse einen Apfel",
"I eat bread .":"Ich esse Brot",
"I eat the apple .":"Ich esse den Apfel",
"I eat the bread .":"Ich esse das Brot",
"Ich bin ein Junge .":"I am a boy",
"Ich bin ein Kind .":"I am a child",
"Ich bin ein Mann .":"I am a man",
"Ich bin ein Mädchen .":"I am a girl",
"Ich bin eine Frau .":"I am a woman",
"Ich esse .":"I eat",
"Ich esse Brot .":"I eat bread",
"Ich esse das Brot .":"I eat the bread",
"Ich esse den Apfel .":"I eat the apple",
"Ich esse einen Apfel .":"I eat an apple",
"Ich trinke .":"I drink",
"Ich trinke das Wasser .":"I drink the water",
"Ich trinke die Milch .":"I drink the milk",
"Ich trinke Milch .":"I drink milk",
"Ich trinke Wasser .":"I drink water",
"She drinks .":"Sie trinkt",
"She drinks milk .":"Sie trinkt Milch",
"She drinks the milk .":"Sie trinkt die Milch",
"She drinks the water .":"Sie trinkt das Wasser",
"She drinks water .":"Sie trinkt Wasser",
"She eats .":"Sie isst",
"She eats an apple .":"Sie isst einen Apfel",
"She eats bread .":"Sie isst Brot",
"She eats the apple .":"Sie isst den Apfel",
"She eats the bread .":"Sie isst das Brot",
"She is a child .":"Sie ist ein Kind",
"She is a girl .":"Sie ist ein Madchen",
"She is a woman .":"Sie ist eine Frau",
"She is drinking .":"Sie trinkt",
"She is drinking milk .":"Sie trinkt Milch",
"She is drinking the milk .":"Sie trinkt die Milch",
"She is drinking the water .":"Sie trinkt das Wasser",
"She is drinking water .":"Sie trinkt Wasser",
"She is eating .":"Sie isst",
"She is eating an apple .":"Sie isst einen Apfel",
"She is eating bread .":"Sie isst Brot",
"She is eating the apple .":"Sie isst den Apfel",
"She is eating the bread .":"Sie isst das Brot",
"Sie isst .":"She eats",
"Sie isst Brot .":"She eats bread",
"Sie isst das Brot .":"She eats the bread",
"Sie isst den Apfel .":"She eats the apple",
"Sie isst einen Apfel .":"She eats an apple",
"Sie ist ein Kind .":"She is a child",
"Sie ist ein Mädchen .":"She is a girl",
"Sie ist eine Frau .":"She is a woman",
"Sie trinkt .":"She drinks",
"Sie trinkt das Wasser .":"She drinks the water",
"Sie trinkt die Milch .":"She drinks the milk",
"Sie trinkt Milch .":"She drinks milk",
"Sie trinkt Wasser .":"She drinks water",
"The boy drinks .":"Der Junge trinkt",
"The boy drinks milk .":"Der Junge trinkt Milch",
"The boy drinks the milk .":"Der Junge trinkt die Milch",
"The boy drinks the water .":"Der Junge trinkt das Wasser",
"The boy drinks water .":"Der Junge trinkt Wasser",
"The boy eats .":"Der Junge isst",
"The boy eats an apple .":"Der Junge isst einen Apfel",
"The boy eats bread .":"Der Junge isst Brot",
"The boy eats the apple .":"Der Junge isst den Apfel",
"The boy eats the bread .":"Der Junge isst das Brot",
"The boy is a child .":"Der Junge ist ein Kind",
"The boy is drinking .":"Der Junge trinkt",
"The boy is drinking milk .":"Der Junge trinkt Milch",
"The boy is drinking the milk .":"Der Junge trinkt die Milch",
"The boy is drinking the water .":"Der Junge trinkt das Wasser",
"The boy is drinking water .":"Der Junge trinkt Wasser",
"The boy is eating .":"Der Junge isst",
"The boy is eating an apple .":"Der Junge isst einen Apfel",
"The boy is eating bread .":"Der Junge isst Brot",
"The boy is eating the apple .":"Der Junge isst den Apfel",
"The boy is eating the bread .":"Der Junge isst das Brot",
"The boy":"Der Junge",
"The bread is good .":"Das Brot ist gut",
"The child drinks .":"Das Kind trinkt",
"The child drinks milk .":"Das Kind trinkt Milch",
"The child drinks the milk .":"Das Kind trinkt die Milch",
"The child drinks the water .":"Das Kind trinkt das Wasser",
"The child drinks water .":"Das Kind trinkt Wasser",
"The child eats .":"Das Kind isst",
"The child eats an apple .":"Das Kind isst einen Apfel",
"The child eats bread .":"Das Kind isst Brot",
"The child eats the apple .":"Das Kind isst den Apfel",
"The child eats the bread .":"Das Kind isst das Brot",
"The child is a boy .":"Das Kind ist ein Junge",
"The child is a girl .":"Das Kind ist ein Madchen",
"The child is drinking .":"Das Kind trinkt",
"The child is drinking milk .":"Das Kind trinkt Milch",
"The child is drinking the milk .":"Das Kind trinkt die Milch",
"The child is drinking the water .":"Das Kind trinkt das Wasser",
"The child is drinking water .":"Das Kind trinkt Wasser",
"The child is eating .":"Das Kind isst",
"The child is eating an apple .":"Das Kind isst einen Apfel",
"The child is eating bread .":"Das Kind isst Brot",
"The child is eating the apple .":"Das Kind isst den Apfel",
"The child is eating the bread .":"Das Kind isst das Brot",
"The child":"Das Kind",
"The girl drinks .":"Das Madchen trinkt",
"The girl drinks milk .":"Das Madchen trinkt Milch",
"The girl drinks the milk .":"Das Madchen trinkt die Milch",
"The girl drinks the water .":"Das Madchen trinkt das Wasser",
"The girl drinks water .":"Das Madchen trinkt Wasser",
"The girl eats .":"Das Madchen isst",
"The girl eats an apple .":"Das Madchen isst einen Apfel",
"The girl eats bread .":"Das Madchen isst Brot",
"The girl eats the apple .":"Das Madchen isst den Apfel",
"The girl eats the bread .":"Das Madchen isst das Brot",
"The girl is a child .":"Das Madchen ist ein Kind",
"The girl is drinking .":"Das Madchen trinkt",
"The girl is drinking milk .":"Das Madchen trinkt Milch",
"The girl is drinking the milk .":"Das Madchen trinkt die Milch",
"The girl is drinking the water .":"Das Madchen trinkt das Wasser",
"The girl is drinking water .":"Das Madchen trinkt Wasser",
"The girl is eating .":"Das Madchen isst",
"The girl is eating an apple .":"Das Madchen isst einen Apfel",
"The girl is eating bread .":"Das Madchen isst Brot",
"The girl is eating the apple .":"Das Madchen isst den Apfel",
"The girl is eating the bread .":"Das Madchen isst das Brot",
"The girl":"Das Madchen",
"The man drinks .":"Der Mann trinkt",
"The man drinks milk .":"Der Mann trinkt Milch",
"The man drinks the milk .":"Der Mann trinkt die Milch",
"The man drinks the water .":"Der Mann trinkt das Wasser",
"The man drinks water .":"Der Mann trinkt Wasser",
"The man eats .":"Der Mann isst",
"The man eats an apple .":"Der Mann isst einen Apfel",
"The man eats bread .":"Der Mann isst Brot",
"The man eats the apple .":"Der Mann isst den Apfel",
"The man eats the bread .":"Der Mann isst das Brot",
"The man is drinking .":"Der Mann trinkt",
"The man is drinking milk .":"Der Mann trinkt Milch",
"The man is drinking the milk .":"Der Mann trinkt die Milch",
"The man is drinking the water .":"Der Mann trinkt das Wasser",
"The man is drinking water .":"Der Mann trinkt Wasser",
"The man is eating .":"Der Mann isst",
"The man is eating an apple .":"Der Mann isst einen Apfel",
"The man is eating bread .":"Der Mann isst Brot",
"The man is eating the apple .":"Der Mann isst den Apfel",
"The man is eating the bread .":"Der Mann isst das Brot",
"The man":"Der Mann",
"The milk is good .":"Die Milch ist gut",
"The woman drinks .":"Die Frau trinkt",
"The woman drinks milk .":"Die Frau trinkt Milch",
"The woman drinks the milk .":"Die Frau trinkt die Milch",
"The woman drinks the water .":"Die Frau trinkt das Wasser",
"The woman drinks water .":"Die Frau trinkt Wasser",
"The woman eats .":"Die Frau isst",
"The woman eats an apple .":"Die Frau isst einen Apfel",
"The woman eats bread .":"Die Frau isst Brot",
"The woman eats the apple .":"Die Frau isst den Apfel",
"The woman eats the bread .":"Die Frau isst das Brot",
"The woman is drinking .":"Die Frau trinkt",
"The woman is drinking milk .":"Die Frau trinkt Milch",
"The woman is drinking the milk .":"Die Frau trinkt die Milch",
"The woman is drinking the water .":"Die Frau trinkt das Wasser",
"The woman is drinking water .":"Die Frau trinkt Wasser",
"The woman is eating .":"Die Frau isst",
"The woman is eating an apple .":"Die Frau isst einen Apfel",
"The woman is eating bread .":"Die Frau isst Brot",
"The woman is eating the apple .":"Die Frau isst den Apfel",
"The woman is eating the bread .":"Die Frau isst das Brot",
"The woman":"Die Frau",
"You are a boy .":"Du bist ein Junge",
"You are a child .":"Du bist ein Kind",
"You are a girl .":"Du bist ein Madchen",
"You are a man .":"Du bist ein Mann",
"You are a woman .":"Du bist eine Frau",
"You are drinking .":"Du trinkst",
"You are drinking milk .":"Du trinkst Milch",
"You are drinking the milk .":"Du trinkst die Milch",
"You are drinking the water .":"Du trinkst das Wasser",
"You are drinking water .":"Du trinkst Wasser",
"You are eating .":"Du isst",
"You are eating an apple .":"Du isst einen Apfel",
"You are eating bread .":"Du isst Brot",
"You are eating the apple .":"Du isst den Apfel",
"You are eating the bread .":"Du isst das Brot",
"You drink .":"Du trinkst",
"You drink milk .":"Du trinkst Milch",
"You drink the milk .":"Du trinkst die Milch",
"You drink the water .":"Du trinkst das Wasser",
"You drink water .":"Du trinkst Wasser",
"You eat .":"Du isst",
"You eat an apple .":"Du isst einen Apfel",
"You eat bread .":"Du isst Brot",
"You eat the apple .":"Du isst den Apfel",
"You eat the bread .":"Du isst das Brot",
};
