let closeBtn = document.querySelector("#close-btn");
let openBtn = document.querySelector("#open-btn");
let sideNavDiv = document.querySelector(".navigation");
let sideNav = document.querySelector("#side-nav");
openBtn.addEventListener("click",()=>{
	sideNav.style.display="flex";
	sideNavDiv.style.width="100%";
	sideNavDiv.style.height="100vh";
	openBtn.style.display="none";
	closeBtn.style.display="block";
	sideNav.style.opacity="1";
});
closeBtn.addEventListener("click",()=>{
	sideNav.style.display="none";
	sideNav.style.opacity="0";
	openBtn.style.display="block"
	sideNavDiv.style.width="0%";
	closeBtn.style.display="none";
});