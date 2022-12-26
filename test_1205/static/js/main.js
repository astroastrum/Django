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

// requestAnimationFrame
tick();
function tick() {
  requestAnimationFrame(tick);
}

// 날짜
const date = new Date();
const year = date.getFullYear();

// HTML
document.querySelector('#log').innerHTML = '지금은 ${year}년입니다.';

const date = new Date();
const month = date.getMonth() + 1;
const day = date.getDate();

// time
const date = new Date();
const hour = date.getHours();
const minutes = date.getMinutes();
const seconds = date.getSeconds();

const num1 = Date.parse('2020/12/25');
console.log(num1);

const num2 = Date.parse('12 25 2020');
console.log(num2);


const num = Date.now();
console.log(num); 

// 스크롤
window.addEventListener('scroll', () => {
  console.log('스크롤', window.scrollX, window.scrollY);
});

const date = new Date();
const hour = date.getHours();
const minutes = date.getMinutes();
const seconds = date.getSeconds();

const label = '${hour}시${minutes}분${seconds}초';