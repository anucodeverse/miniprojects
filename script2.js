const questions=[
{
	question:"which is the largest animal in the world",
	answers:[
			{text:"shark",correct:false},
			{text:"Blue whale",correct:true},
			{text:"Elephant",correct:false},
			{text:"Giraffe",correct:false},

		]

},
{
	question:"which is the smallest country in the world",
	answers:[
			{text:"Vatican City",correct:true},
			{text:"Bhutan",correct:false},
			{text:"Nepal",correct:false},
			{text:"srilanka",correct:false},

		]

},
{
	question:"which is the longest river in the world",
	answers:[
			{text:"Ganga",correct:false},
			{text:"Godavari",correct:false},
			{text:"Nile",correct:true},
			{text:"kaveri",correct:false},

		]

},
{
	question:"which is the largest desert in the world",
	answers:[
			{text:"kalahari",correct:false},
			{text:"Gobi",correct:true},
			{text:"Sahara",correct:false},
			{text:"Antarctica",correct:true},

		]

},
{
	question:"which is the smallest content in the world",
	answers:[
			{text:"Asia",correct:false},
			{text:"Australia",correct:true},
			{text:"Arctic",correct:false},
			{text:"Africa",correct:false},

		]

}


	];
const questionElement=document.getElementById("questions");
const answerButton=document.getElementById("ansbtn");
const nextButton=document.getElementById("next-btn");

