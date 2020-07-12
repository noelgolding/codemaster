// add event listeners to all of the code inputs
const code_lines = [];

window.addEventListener('load', (e) => {
  toggleTitleBar()
  document.querySelectorAll('.code').forEach((elem) => {
    addCodeLine(elem);
  });
});

document.addEventListener("fullscreenchange", (e) => {
  toggleTitleBar();
});

function toggleTitleBar() {
  if (isFullScreen()) {
    document.getElementById('cm_titlebar').style.display = 'grid';
    document.querySelector('.fullscreen-button').classList.add('hidden');
  } else {
    document.getElementById('cm_titlebar').style.display = 'none';
    document.querySelector('.fullscreen-button').classList.remove('hidden');
  }
}

function dockSideBar(e, css_selector) {
  const app = document.querySelector(css_selector);
  const elems = [app, e];
  if (app.classList.contains('flipped')) {
    elems.forEach((elem) => {
      elem.classList.remove('flipped');
    });
  } else {
    elems.forEach(elem => {
      elem.classList.add('flipped');
    });
  }
}

function addCodeLine(elem) {
  elem.addEventListener('keydown', code_keydown);
  code_lines.push(elem);
}

function code_keydown(e) {
  // console.log(e);
  switch (e.key) {
    case 'Tab':
      e.preventDefault();
      if (e.shiftKey) {
        untab_code(e.srcElement);
      } else {
        tab_code(e.target);
      }
      break;
    case 'ArrowUp':
      e.preventDefault();
      prev_codeline(e.srcElement);
      break;
    case 'ArrowDown':
      e.preventDefault();
      next_codeline(e.srcElement);
      break;
    case 'ArrowRight':
      if (e.shiftKey) {
        e.preventDefault();
        tab_code(e.srcElement);
      }
      break;
    case 'ArrowLeft':
      if (e.shiftKey) {
        e.preventDefault();
        untab_code(e.srcElement);
      }
      break;
    case 'Enter':
      e.preventDefault();
      if (e.shiftKey) {
        insert_codeline(e.srcElement);
      } else {
        next_codeline(e.srcElement);
      }
      break;
    case 'Delete':
      if (e.shiftKey) {
        e.preventDefault();
        delete_codeline(e.srcElement);
      }
      break;
    case 'Backspace':
    case 'End':
    case 'Home':
    case ' ':
    case '0':
    case '1':
    case '2':
    case '3':
    case '4':
    case '5':
    case '6':
    case '7':
    case '8':
    case '9':
    case 'a':
    case 'b':
    case 'c':
    case 'd':
    case 'e':
    case 'f':
    case 'g':
    case 'h':
    case 'i':
    case 'j':
    case 'k':
    case 'l':
    case 'm':
    case 'n':
    case 'o':
    case 'p':
    case 'q':
    case 'r':
    case 's':
    case 't':
    case 'u':
    case 'v':
    case 'w':
    case 'x':
    case 'y':
    case 'z':
      break;
    default:
      e.preventDefault();
  }
}

// tab or shift+right arrow
function tab_code(elem) {
  console.log("===TODO===", 'tab', elem);
}

// shift+tab or shift+left arrow
function untab_code(elem) {
  console.log("===TODO===", 'untab', elem);
}

// enter or down arrow
function next_codeline(elem) {
  console.log("===TODO===", 'next', elem);
}

// up arrow
function prev_codeline(elem) {
  console.log("===TODO===", 'prev', elem);
}

// shift+enter
function insert_codeline(elem) {
  console.log("===TODO===", 'insert', elem);
}

// shift+delete
function delete_codeline(elem) {
  console.log("===TODO===", 'delete', elem);
}
