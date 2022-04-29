function deleteSprout(sproutID) {
   fetch('/delete-sprout', {
      method: 'POST',
      body: JSON.stringify({ sproutId: sproutID})
   }).then((_res) => {
      window.location.href = "/";
   });
}