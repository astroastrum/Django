const date = new Date();
const hour = date.getHours();
const minutes = date.getMinutes();
const seconds = date.getSeconds();

const label = '${hour}시${minutes}분${seconds}초';

// 이미지 로딩
const imgJ = document.querySelector
('#myImageJ');
imgA.src = 'images/photo_j.jpg';

const imgK = document.querySelector
('#myImageK');
imgB.src = 'images/photo_k.jpg';


// 날씨
const weatherInformation =
document.querySelector('#weather-information');

// <p id="weather-information">비<span class="temperature">(16)</span></p>console.log(weatherInformation.outerHTML);

// <p id="weather-information"></p>
weatherInformation.outerHTML = '<img src="sample-image.png">';