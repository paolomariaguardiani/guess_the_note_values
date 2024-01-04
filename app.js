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
