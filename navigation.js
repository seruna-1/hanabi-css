const htmlBody = document.querySelector("body");

const buttonShowSectionIndex = document.getElementById("toggleSectionIndex");
buttonShowSectionIndex.addEventListener("click", toggleSectionIndex);

const buttonGoTop = document.getElementById("goTopButton");
buttonGoTop.addEventListener("click", goTop);

const sectionIndex = document.getElementById("sectionIndex");
sectionIndex.style.setProperty("display", "none");



/* Scrolls page to top */
function goTop ()
{
	document.querySelector("header").scrollIntoView();
	return;
}



/*



*/
function generateSectionIndex ()
{
	const headings = document.querySelectorAll("h1");


	for ( let i=0; i < headings.length; i++ )
	{
		headings[i].setAttribute("id", "head" + i);
		
		/* Each anchor is inside a paragraph */
		let section = document.createElement("p");

		let anchor = document.createElement("a");
		
		anchor.setAttribute("href", "#" + headings[i].getAttribute("id"));

		anchor.textContent = headings[i].textContent;

		anchor.addEventListener("click", scrollToHeading);

		section.appendChild(anchor);

		sectionIndex.appendChild(section);
	}

	/* sectionIndex element is hidden by default */
	sectionIndex.style.display = "none";
	
	return;
}


function toggleSectionIndex ()
{
	if ( sectionIndex.style.display === "none" )
	{
		document.querySelector("main").style.display = "none";
				
		sectionIndex.style.display = "grid";
	}
	

	else
	{
		document.querySelector("main").style.display = "grid";
		
		sectionIndex.style.display = "none";
	}

	
	return;
}



function toggleIdiomIndex ()
{
	

	return;
}



/*
Toggles element [main] by element with id [substituteId].
*/
function toggleMainContent ( substituteId )
{
	return;
}



/*

This function is called when anchor in [section index] is clicked.

On execution, [section index] is hidden and the page view is scrolled to heading associated with the anchor that was clicked.

The argument [event] is used to determine the heading to where the page view will be scrolled to.

*/
function scrollToHeading ( event )
{
	/* Close section index if it is open */
	if ( sectionIndex.style.display === "grid" ) { toggleSectionIndex(); }


	/*
	Pass the [href] attribute of anchor clicked as input to function [querySelector].

	[href] is an id, like [#head1] for example, so [querySelector] returns an object [Element].

	On top of this object, we use the method [scrollIntoView].
	*/
	document.querySelector(event.target.getAttribute("href")).scrollIntoView();

	return;
}



generateSectionIndex();

