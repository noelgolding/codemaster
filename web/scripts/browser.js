// TODO : disable F11 (keyboard shortcut for fullscreen)
// TODO : disable (keyboard shortcut for inspector/javascript console)

function toggleFullScreen() {
  try {
    if (isFullScreen()) {
      closeFullscreen();
    } else {
      openFullscreen();
    }
  } catch (e) {
    // do nothing
  }
}

function isFullScreen() {
  // FIXME
  return !(
    (document.fullScreenElement !== undefined && document.fullScreenElement === null) ||
    (document.msFullscreenElement !== undefined && document.msFullscreenElement === null) ||
    (document.mozFullScreen !== undefined && !document.mozFullScreen) ||
    (document.webkitIsFullScreen !== undefined && !document.webkitIsFullScreen)
  )
}

/* View in fullscreen */
function openFullscreen() {
  const elem = document.documentElement;
  if (elem.requestFullscreen) {
    elem.requestFullscreen();
  } else if (elem.mozRequestFullScreen) {
    /* Firefox */
    elem.mozRequestFullScreen();
  } else if (elem.webkitRequestFullscreen) {
    /* Chrome, Safari and Opera */
    elem.webkitRequestFullscreen(Element.ALLOW_KEYBOARD_INPUT);
  } else if (elem.msRequestFullscreen) {
    /* IE/Edge */
    elem.msRequestFullscreen();
  }
}

/* Close fullscreen */
function closeFullscreen() {
  if (document.exitFullscreen) {
    document.exitFullscreen();
  } else if (document.mozCancelFullScreen) {
    /* Firefox */
    document.mozCancelFullScreen();
  } else if (document.webkitExitFullscreen) {
    /* Chrome, Safari and Opera */
    document.webkitExitFullscreen();
  } else if (document.msExitFullscreen) {
    /* IE/Edge */
    document.msExitFullscreen();
  }
}
