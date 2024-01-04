const images = [
    "images/fig_01a.png",
    "images/fig_01b.png",
    "images/fig_02a.png",
    "images/fig_02b.png",
    "images/fig_03a.png",
    "images/fig_03b.png",
    "images/fig_04a.png",
    "images/fig_04b.png",
    "images/fig_05a.png",
    "images/fig_05b.png",
    "images/fig_06a.png",
    "images/fig_06b.png"
]

// Thanks to https://www.educative.io/answers/how-to-shuffle-an-array-in-javascript
let clonedImages = images.slice(0);

function shuffleArray(array) {
    let len = array.length,
    currentIndex;
    for (currentIndex = len - 1; currentIndex > 0; currentIndex--) {
        let randIndex = Math.floor(Math.random() * (currentIndex + 1) );
        var temp = array[currentIndex];
        array[currentIndex] = array[randIndex];
        array[randIndex] = temp;
    }
}

let sortedImage = ""

function changeImage() {
    // Mescolo le immagini
    shuffleArray(clonedImages);

    image = document.getElementById("image_question");
    //let index = Math.trunc(Math.random() * images.length);
    
    if (clonedImages.length > 0) {
        // selezione l'ultima immagine dall'array clonato e rimescolato
        sortedImage = clonedImages.pop();
        image.src = sortedImage;
        console.log(sortedImage);
    }
    else {
        // Se ho eliminato tutte le immagini dall'array clonato lo ricreo!
        clonedImages = images.slice(0);
    }
    console.log(clonedImages)
}


function checkNames(number) {
    // console.log("from check()");
    // console.log(number);
    // console.log(sortedImage);
    // if ((sortedImage == "images\fig_01a.png" || sortedImage == "images\fig_01b.png") && number == 11) {
    //     console.log("Evviva!!!");
    // }
    switch(number) {
        case 11:
            if (sortedImage == "images/fig_01a.png" || sortedImage == "images/fig_01b.png"){
                console.log("Evviva!!!");
            }
            else {
                console.log("Sbagliato");
            }
            break;       
        case 12:
            if (sortedImage == "images/fig_02a.png" || sortedImage == "images/fig_02b.png"){
                console.log("Evviva!!!");
            }
            else {
                console.log("Sbagliato");
            }    
            break;   
        case 13:
            if (sortedImage == "images/fig_03a.png" || sortedImage == "images/fig_03b.png"){
                console.log("Evviva!!!");
            }
            else {
                console.log("Sbagliato");
            }    
            break;   
        case 14:
            if (sortedImage == "images/fig_04a.png" || sortedImage == "images/fig_04b.png"){
                console.log("Evviva!!!");
            }
            else {
                console.log("Sbagliato");
            }    
            break;   
        case 15:
            if (sortedImage == "images/fig_05a.png" || sortedImage == "images/fig_05b.png"){
                console.log("Evviva!!!");
            }
            else {
                console.log("Sbagliato");
            }    
            break;   
        case 16:
            if (sortedImage == "images/fig_06a.png" || sortedImage == "images/fig_06b.png"){
                console.log("Evviva!!!");
            }
            else {
                console.log("Sbagliato");
            }    
            break;   
        default:
            console.log("Something went wrong");
    }
}
