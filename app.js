// carico i suoni
let sound_click = new Howl({
    src: ['audio/click_1.wav']
});
let sound_bleep = new Howl({
    src: ['audio/bleep_soft.wav']
});
let sound_error = new Howl({
    src: ['audio/sound_error.wav']
});
let sound_ok = new Howl({
    src: ['audio/blip-131856.mp3']
})
let sound_reload = new Howl({
    src: ['audio/new_game.wav']
})

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

let sortedImage = ""
let points = 0;
let checked = true;
guess = 0;
counter = 0;
voto = 0;
let display_tests = document.getElementById("tests");
let display_points = document.getElementById("points");
let display_voto = document.getElementById("voto");

function italianEnglish1() {
    sound_bleep.play();
    setTimeout(function() {
        window.location.assign("index.html");
        console.log("ciao da italianEnglish1()!")
    }, 1000);
}

function italianEnglish2() {
    sound_bleep.play();
    setTimeout(function() {
        window.location.assign("english.html");
        console.log("ciao da italianEnglish2()!")
    }, 1000);
}


// Thanks to https://www.educative.io/answers/how-to-shuffle-an-array-in-javascript
let clonedImages = images.slice(0);

function shuffleArray(array) {
    let len = array.length,
        currentIndex;
    for (currentIndex = len - 1; currentIndex > 0; currentIndex--) {
        let randIndex = Math.floor(Math.random() * (currentIndex + 1));
        var temp = array[currentIndex];
        array[currentIndex] = array[randIndex];
        array[randIndex] = temp;
    }
}

function changeImage() {
    // Mescolo le immagini
    sound_click.play();
    shuffleArray(clonedImages);
    checked = false;
    guess = 0;

    image = document.getElementById("image_question");
    //let index = Math.trunc(Math.random() * images.length);

    if (clonedImages.length > 0) {
        // selezione l'ultima immagine dall'array clonato e rimescolato
        sortedImage = clonedImages.pop();
        image.src = sortedImage;
    }
    else {
        // Se ho eliminato tutte le immagini dall'array clonato lo ricreo!
        clonedImages = images.slice(0);
        // selezione l'ultima immagine dall'array clonato e rimescolato
        sortedImage = clonedImages.pop();
        image.src = sortedImage;
    }
    console.log(counter);
    if (counter == 13) {
        console.log("ho eseguito 12 prove");
        sound_bleep.play();
        test02();
    }
    if (counter == 25) {
        console.log("ho eseguito 24 prove");
        sound_bleep.play();
        test03();
    }
    if (counter == 37) {
        console.log("ho eseguito 36 prove");
        sound_bleep.play();
        test01(); 
    }
}


function checkNames(number) {
    switch (number) {
        case 1:
            if (sortedImage == "images/fig_01a.png" || sortedImage == "images/fig_01b.png") {
                guess = 1;
            }
            else {
                guess = 0;
            }
            break;
        case 2:
            if (sortedImage == "images/fig_02a.png" || sortedImage == "images/fig_02b.png") {
                guess = 1;
            }
            else {
                guess = 0;
            }
            break;
        case 3:
            if (sortedImage == "images/fig_03a.png" || sortedImage == "images/fig_03b.png") {
                guess = 1;
            }
            else {
                guess = 0;
            }
            break;
        case 4:
            if (sortedImage == "images/fig_04a.png" || sortedImage == "images/fig_04b.png") {
                guess = 1;
            }
            else {
                guess = 0;
            }
            break;
        case 5:
            if (sortedImage == "images/fig_05a.png" || sortedImage == "images/fig_05b.png") {
                guess = 1;
            }
            else {
                guess = 0;
            }
            break;
        case 6:
            if (sortedImage == "images/fig_06a.png" || sortedImage == "images/fig_06b.png") {
                guess = 1;
            }
            else {
                guess = 0;
            }
            break;
        default:
            console.log("Something went wrong");
    }
    if (guess == 1 && checked == false) {
        sound_ok.play();
        counter++;
        points++;
        updateScore();
        checked = true;
    }
    if (guess == 0 && checked == false) {
        sound_error.play();
        counter++;
        updateScore();
        checked = true;
    }
}

function updateScore() {
        display_tests.innerHTML = "TEST: " + counter;
        display_points.innerHTML = "POINTS: " + points;
        voto = points * 10 / counter;
        display_voto.innerHTML = "SCORE: " + voto.toFixed(2);
}

// thanks to: https://deepdeveloper.in/show-hide-multiple-divs-in-javascript/
function test01() {
    // seleziono una nuova immagine
    changeImage();
    sound_bleep.play();
    // nascondo il test02 e il test03
    var divs2 = document.getElementsByClassName("test02");
    var divs3 = document.getElementsByClassName("test03");
    for (var i = 0; i < divs2.length; i++) {
        divs2[i].style.display = "none";
        divs3[i].style.display = "none";
    }

    // mostro il test01
    var divs1 = document.getElementsByClassName("test01");
    for (var i = 0; i < divs1.length; i++) {
        divs1[i].style.display = "block";
    }
}

function test02() {
    // seleziono una nuova immagine
    changeImage();
    sound_bleep.play();
    // nascondo il test02 e il test03
    var divs1 = document.getElementsByClassName("test01");
    var divs3 = document.getElementsByClassName("test03");
    for (var i = 0; i < divs1.length; i++) {
        divs1[i].style.display = "none";
        divs3[i].style.display = "none";
    }

    // mostro il test01
    var divs2 = document.getElementsByClassName("test02");
    for (var i = 0; i < divs2.length; i++) {
        divs2[i].style.display = "block";
    }
}

function test03() {
    // seleziono una nuova immagine
    changeImage();
    sound_bleep.play();
    // nascondo il test01 e il test02
    var divs1 = document.getElementsByClassName("test01");
    var divs2 = document.getElementsByClassName("test02");
    for (var i = 0; i < divs1.length; i++) {
        divs1[i].style.display = "none";
        divs2[i].style.display = "none";
    }

    // mostro il test01
    var divs3 = document.getElementsByClassName("test03");
    for (var i = 0; i < divs3.length; i++) {
        divs3[i].style.display = "block";
    }
}

function reloadPage() {
    sound_reload.play();
    setTimeout(function() {
        window.location.reload();
    }, 3000);
}

// UTILIZZO DELLA FRECCIA DESTRA E DELLE LETTERE U I O J K L AL POSTO DEI BOTTONI
window.addEventListener('keydown', function(event) {
    // bottone next: freccia a destra oppure lettera f
    if (event.which === 70 || event.which === 39) { changeImage(); }

    // seguono i comandi per "cliccare" le varie risposte
    if (event.which === 85) { checkNames(1); }
    if (event.which === 73) { checkNames(2); }
    if (event.which === 79) { checkNames(3); }

    if (event.which === 74) { checkNames(4); }
    if (event.which === 75) { checkNames(5); }
    if (event.which === 76) { checkNames(6); }

    // segue il comando F5 per fare il reload della pagina
    if (event.which === 53) { reloadPage(); }

}, false);
