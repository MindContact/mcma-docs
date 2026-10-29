// Contact form of mindcontact.app (copied from mindcontact-net/site/assets/js/site.js): posts to mindcontact-forms with fetch and shows the outcome in the page.
// Without JavaScript the form does a plain POST and the service redirects back (_next).
(function () {
  var form = document.querySelector("[data-contact-form]");
  if (!form) return;
  var status = form.querySelector(".form-status");
  var button = form.querySelector("button[type=submit]");

  function say(text, error) {
    status.textContent = text;
    status.classList.toggle("is-error", !!error);
  }

  // Back from a no-JavaScript POST: the service redirects here with ?inviato or ?sent.
  if (/[?&](inviato|sent)\b/.test(location.search)) {
    say(form.dataset.sent);
    history.replaceState(null, "", location.pathname + location.hash);
  }

  form.addEventListener("submit", function (e) {
    if (!window.fetch || !window.FormData) return;
    e.preventDefault();
    button.disabled = true;
    say(form.dataset.sending);
    fetch(form.action, {
      method: "POST",
      headers: { "Accept": "application/json" },
      body: new URLSearchParams(new FormData(form))
    }).then(function (r) {
      if (!r.ok) throw new Error(r.status);
      form.reset();
      say(form.dataset.sent);
    }).catch(function () {
      say(form.dataset.error, true);
    }).finally(function () {
      button.disabled = false;
    });
  });
})();

// Privacy notice: links to #privacy open the <dialog>; a click on the backdrop or Esc closes it.
(function () {
  var modal = document.getElementById("privacy-form");
  if (!modal || typeof modal.showModal !== "function") return;
  document.querySelectorAll('a[href="#privacy-form"]').forEach(function (link) {
    link.addEventListener("click", function (e) {
      e.preventDefault();
      modal.showModal();
    });
  });
  modal.addEventListener("click", function (e) {
    if (e.target === modal || e.target.closest('a[href="#contatti"]')) modal.close();
  });
})();
