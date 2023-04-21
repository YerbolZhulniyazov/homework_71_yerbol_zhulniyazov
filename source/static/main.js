
document.addEventListener('DOMContentLoaded', function() {
const likeForm = document.querySelector('#form-like');
const dislikeForm = document.querySelector('#form-dislike');
console.log(dislikeForm)

likeForm.addEventListener('submit', e => {
  e.preventDefault();
  const img = likeForm.querySelector('img');
  img.src = '/static/images/liked.PNG';
  fetch(likeForm.action, {
    method: 'POST',
    body: new FormData(likeForm),
    headers: {
      'X-CSRFToken': likeForm.querySelector('input[name="csrfmiddlewaretoken"]').value
    }
  }).then(response => {
    if (response.ok) {
      location.reload();
    } else {
      img.src = '/static/images/like.PNG';
    }
  });
});

dislikeForm.addEventListener('submit', e => {
  e.preventDefault();
  const img = dislikeForm.querySelector('img');
  img.src = '/static/images/like.PNG';
  fetch(dislikeForm.action, {
    method: 'POST',
    body: new FormData(dislikeForm),
    headers: {
      'X-CSRFToken': dislikeForm.querySelector('input[name="csrfmiddlewaretoken"]').value
    }
  }).then(response => {
    if (response.ok) {
      location.reload();
    } else {
      img.src = '/static/images/liked.PNG';
    }
  });
});

});
