const box = document.querySelector('#box');
// 배경을 초록색으로 변경 
box.style.backgroundColor = 'green';

// HTML
// <p id="december">Christmas in South Korea</p>
const december = document.querySelector('#december');
// color 속성 변경
december.style.color = 'white';
// font-size 속성 변경
december.style.fontsize = '10px';

const strokeColor = '#228B22';
// -webkit-text-stroke 속성 변경
december.style.webkitTextStroke = '2px ${strokeColor}';
// text-stroke 속성 변경
december.style.textStroke = '2px ${strokeColor}';
// text-shadow 속성 변경
december.style.textShadow = '7px 7px 0 #90EE90';
