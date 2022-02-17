// la etiqueta script que llama a este script
var thisScript = document.currentScript;

// los lenguajes que puedo traducir
var languages = [
  { lang: "af", title: "afrikaans" },
  { lang: "sq", title: "albanian" },
  { lang: "am", title: "amharic" },
  { lang: "ar", title: "arabic" },
  { lang: "hy", title: "armenian" },
  { lang: "az", title: "azerbaijani" },
  { lang: "eu", title: "basque" },
  { lang: "be", title: "belarusian" },
  { lang: "bn", title: "bengali" },
  { lang: "bs", title: "bosnian" },
  { lang: "bg", title: "bulgarian" },
  { lang: "ca", title: "catalan" },
  { lang: "ceb", title: "cebuano" },
  { lang: "ny", title: "chichewa" },
  { lang: "zh-CN", title: "chinese (simplified)" },
  { lang: "zh-TW", title: "chinese (traditional)" },
  { lang: "co", title: "corsican" },
  { lang: "hr", title: "croatian" },
  { lang: "cs", title: "czech" },
  { lang: "da", title: "danish" },
  { lang: "nl", title: "dutch" },
  { lang: "en", title: "english" },
  { lang: "eo", title: "esperanto" },
  { lang: "et", title: "estonian" },
  { lang: "tl", title: "filipino" },
  { lang: "fi", title: "finnish" },
  { lang: "fr", title: "french" },
  { lang: "fy", title: "frisian" },
  { lang: "gl", title: "galician" },
  { lang: "ka", title: "georgian" },
  { lang: "de", title: "german" },
  { lang: "el", title: "greek" },
  { lang: "gu", title: "gujarati" },
  { lang: "ht", title: "haitian creole" },
  { lang: "ha", title: "hausa" },
  { lang: "haw", title: "hawaiian" },
  { lang: "iw", title: "hebrew" },
  { lang: "hi", title: "hindi" },
  { lang: "hmn", title: "hmong" },
  { lang: "hu", title: "hungarian" },
  { lang: "is", title: "icelandic" },
  { lang: "ig", title: "igbo" },
  { lang: "id", title: "indonesian" },
  { lang: "ga", title: "irish" },
  { lang: "it", title: "italian" },
  { lang: "ja", title: "japanese" },
  { lang: "jw", title: "javanese" },
  { lang: "kn", title: "kannada" },
  { lang: "kk", title: "kazakh" },
  { lang: "km", title: "khmer" },
  { lang: "ko", title: "korean" },
  { lang: "ku", title: "kurdish (kurmanji)" },
  { lang: "ky", title: "kyrgyz" },
  { lang: "lo", title: "lao" },
  { lang: "la", title: "latin" },
  { lang: "lv", title: "latvian" },
  { lang: "lt", title: "lithuanian" },
  { lang: "lb", title: "luxembourgish" },
  { lang: "mk", title: "macedonian" },
  { lang: "mg", title: "malagasy" },
  { lang: "ms", title: "malay" },
  { lang: "ml", title: "malayalam" },
  { lang: "mt", title: "maltese" },
  { lang: "mi", title: "maori" },
  { lang: "mr", title: "marathi" },
  { lang: "mn", title: "mongolian" },
  { lang: "my", title: "myanmar (burmese)" },
  { lang: "ne", title: "nepali" },
  { lang: "no", title: "norwegian" },
  { lang: "ps", title: "pashto" },
  { lang: "fa", title: "persian" },
  { lang: "pl", title: "polish" },
  { lang: "pt", title: "portuguese" },
  { lang: "pa", title: "punjabi" },
  { lang: "ro", title: "romanian" },
  { lang: "ru", title: "russian" },
  { lang: "sm", title: "samoan" },
  { lang: "gd", title: "scots gaelic" },
  { lang: "sr", title: "serbian" },
  { lang: "st", title: "sesotho" },
  { lang: "sn", title: "shona" },
  { lang: "sd", title: "sindhi" },
  { lang: "si", title: "sinhala" },
  { lang: "sk", title: "slovak" },
  { lang: "sl", title: "slovenian" },
  { lang: "so", title: "somali" },
  { lang: "es", title: "español" },
  { lang: "su", title: "sundanese" },
  { lang: "sw", title: "swahili" },
  { lang: "sv", title: "swedish" },
  { lang: "tg", title: "tajik" },
  { lang: "ta", title: "tamil" },
  { lang: "te", title: "telugu" },
  { lang: "th", title: "thai" },
  { lang: "tr", title: "turkish" },
  { lang: "uk", title: "ukrainian" },
  { lang: "ur", title: "urdu" },
  { lang: "uz", title: "uzbek" },
  { lang: "vi", title: "vietnamese" },
  { lang: "cy", title: "welsh" },
  { lang: "xh", title: "xhosa" },
  { lang: "yi", title: "yiddish" },
  { lang: "yo", title: "yoruba" },
  { lang: "zu", title: "zulu" },
  { lang: "fil", title: "Filipino" },
  { lang: "he", title: "Hebrew" },
];

// el lenguaje que ha seleccionado el usuario
var lang = "es";

// cuando termina de cargarse la pagina completa
window.onload = function createBotino() {
  if (thisScript) {
    // la carpeta en que se van a poner las imagenes
    var imagesFolder = "./";
    imagesFolder = thisScript.getAttribute("images");
    if (!imagesFolder.endsWith("/")) {
      imagesFolder += "/";
    }

    // el div en que se va a poner el chat
    var div_id = thisScript.getAttribute("div_id");
    if (div_id) {
      var d = document.getElementById(div_id);

      // si se definio por el usuario un div para poner al botino
      if (d) {
        // boton para abrir el botino
        var btn = document.createElement("button");
        btn.className = "open-button";
        btn.onclick = function () {
          openForm();
        };
        var img = document.createElement("img");
        // img.src = imagesFolder + "botino.png";
        img.src = imagesFolder + "language32.png";
        btn.append(img);
        d.append(btn);

        // div en que se muestra el chat con botino
        var botForm = document.createElement("div");
        botForm.className = "chat-popup";
        botForm.id = "botForm";

        //  barra de menu
        var f = document.createElement("form");
        f.action = "#";
        f.className = "form-menu";
        f.onsubmit = function () {
          return closeForm();
        };

        // imagen del lenguaje
        img = document.createElement("img");
        img.className = "icon-chat";
        img.src = imagesFolder + "language.png";
        f.append(img);

        var langs = document.createElement("select");
        langs.id = "langs";
        for (var i = 0; i < languages.length; i++) {
          var option = document.createElement("option");
          option.value = languages[i].lang;
          option.text = languages[i].title;
          if (languages[i].lang === lang) {
            option.selected = true;
          }
          langs.appendChild(option);
        }
        langs.onchange = function (e) {
          lang = e.target.value;
        };
        f.append(langs);

        // boton para cerrar el chat
        btn = document.createElement("button");
        btn.type = "submit";
        btn.className = "btn";
        btn.innerText = "X";
        f.append(btn);

        botForm.append(f);

        // div con el contenido del chat, aqui van todos los mensajes
        var chatContent = document.createElement("div");
        chatContent.className = "chat-content";
        chatContent.id = "chat-content";
        botForm.append(chatContent);

        // formulario en que el usuario escribe el mensaje
        f = document.createElement("form");
        f.id = "botinoForm";
        f.action = "#";
        f.className = "form-container";
        f.onsubmit = function () {
          return sendFormMessage(this);
        };

        // input en que el usuario escribe su mensaje a botino
        var txt = document.createElement("input");
        txt.type = "text";
        txt.placeholder = "Escriba su mensaje...";
        txt.id = "msg";
        txt.className = "msg";
        txt.required = true;
        f.append(txt);

        // boton para enviar el mensaje a botino
        btn = document.createElement("button");
        btn.type = "submit";
        btn.className = "btn";
        img = document.createElement("img");
        img.className = "icon-chat";
        img.src = imagesFolder + "send_msg.png";
        btn.append(img);
        f.append(btn);

        // boton para limpiar el chat
        btn = document.createElement("button");
        btn.type = "button";
        btn.className = "btn cancel";
        btn.onclick = function () {
          clearMessages();
        };
        img = document.createElement("img");
        img.className = "icon-chat";
        img.src = imagesFolder + "clear_chat.png";
        btn.append(img);
        f.append(btn);

        botForm.append(f);

        d.append(botForm);
      }
    }
  }
};

// abrir el chat
function openForm() {
  document.getElementById("botForm").style.display = "block";
}

// cerrar el chat
function closeForm() {
  document.getElementById("botForm").style.display = "none";

  return false;
}

// limpiar los mensajes del chat
function clearMessages() {
  var cnt = document.getElementById("chat-content");
  cnt.innerText = "";
}

// enviar el mensaje de texto del usuario
function sendFormMessage(theForm) {
  if (thisScript) {
    var url = thisScript.getAttribute("url");
    if (url) {
      // Sending and receiving data in JSON format using POST method
      //
      var xhr = new XMLHttpRequest();
      console.log(url);
      xhr.open("POST", url, true);
      xhr.setRequestHeader("Content-Type", "application/json");
      xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
          receiveAnswer(this);
        }
      };
      var data = JSON.stringify({ text: theForm.msg.value, lang: lang });
      xhr.send(data);
    }
  }

  return false;
}

// enviar un mensaje al usuario desde un boton del tipo answer
function sendAnswerMessage(message) {
  if (message && thisScript) {
    var url = thisScript.getAttribute("url");
    if (url) {
      // Sending and receiving data in JSON format using POST method
      //
      var xhr = new XMLHttpRequest();
      xhr.open("POST", url, true);
      xhr.setRequestHeader("Content-Type", "application/json");
      xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
          receiveAnswer(this);
        }
      };
      var data = JSON.stringify({ text: message, lang: lang });
      xhr.send(data);
    }
  }

  return false;
}

// enviar un formulario con datos dinámicos
function sendCustomMessage(theForm) {
  if (thisScript) {
    var url = thisScript.getAttribute("url");
    if (url) {
      // Sending and receiving data in JSON format using POST method
      //
      var xhr = new XMLHttpRequest();
      xhr.open("POST", url, true);
      xhr.setRequestHeader("Content-Type", "application/json");
      xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
          receiveAnswer(this);
        }
      };
      // los datos que voy a enviar al servidor
      var body = [];
      var elements = theForm.elements;
      // recorro todos los elementos del formulario
      for (var i = 0, element; (element = elements[i++]); ) {
        // envio solo los input
        if (["INPUT", "SELECT"].indexOf(element.nodeName) > -1) {
          // envio el id y el value
          body.push({ id: element.id, value: element.value });
        }
      }
      var data = JSON.stringify({ body: body, lang: lang });
      xhr.send(data);
    }
  }

  return false;
}

// recibo la respuesta del usuario
function receiveAnswer(xhr) {
  // convierto la respuesta a json
  var json = JSON.parse(xhr.responseText);
  // almaceno el body de la respuesta
  var bd = null;
  // almaceno el texto de entrada
  var input_text = "";
  if (json) {
    if (json.body) {
      // bd = JSON.parse(json.body.replace(/'/g, '"'));
      bd = JSON5.parse(json.body);
    }
    if (json.input_text) {
      input_text = json.input_text;
    }
  }

  // el folder en que se encuentran las imágenes
  var imagesFolder = "./";
  if (thisScript && thisScript.getAttribute("images")) {
    imagesFolder = thisScript.getAttribute("images");
    if (!imagesFolder.endsWith("/")) {
      imagesFolder += "/";
    }
  }

  // el elemento que contiene los elementos del chat
  var cnt = document.getElementById("chat-content");

  // creo el div con el mensaje del usuario
  var div_msg = document.createElement("div");
  div_msg.className = "user-msg";

  // le pongo la imagen del icono del usuario
  var img = document.createElement("img");
  img.className = "icon-chat";
  img.src = imagesFolder + "user.png";
  // img.src = "data:image/svg+xml;base64," + encodedUser;
  div_msg.append(img);

  // le pongo el texto que envio el usuario
  var p = document.createElement("p");
  p.className = "inner-text";
  p.innerText = input_text;
  div_msg.append(p);

  // adiciono el div con elmensaje del usuario
  cnt.append(div_msg);

  // creo el mensaje de respuesta de botino
  div_msg = document.createElement("div");
  div_msg.className = "bot-msg";

  // creo la imagen de botino
  img = document.createElement("img");
  img.className = "icon-chat";
  img.src = imagesFolder + "botino.png";
  // img.src = "data:image/svg+xml;base64," + encodedBot;
  div_msg.append(img);

  // si la respuesta fue un body
  if (bd && bd.length > 0) {
    // pongo el body en la respuesta
    buildBody(bd, div_msg, imagesFolder);
  } else if (json && json.text) {
    // si la respuesta fue un texto lo pongo en la respuesta
    p = document.createElement("p");
    p.className = "inner-text";
    p.innerText = json.text;
    div_msg.append(p);
  }

  cnt.append(div_msg);

  cnt.scrollTo(0, cnt.scrollHeight);
}

// construyo el body que se le muestra al usuario como respuesta de botino
function buildBody(bd, div_msg, imagesFolder) {
  // para cada elemento de la respuesta de botino
  bd.forEach(function (el) {
    // si el elemento tiene un tag
    if (el.tag) {
      var tg = el.tag.toLowerCase();
      var theTag = null;
      if (tg === "answer" && el.text && el.label) {
        // si el tag es answer
        // creo un form
        theTag = document.createElement("form");
        theTag.action = "#";
        theTag.className = "form-answer";
        // el form envia el texto que tiene el elemento answer
        theTag.onsubmit = function () {
          return sendAnswerMessage(el.text);
        };
        // creo el boton que va a enviar el mensaje a botino
        var btn = document.createElement("button");
        btn.type = "submit";
        btn.className = "btn";
        btn.innerText = el.label;

        // adiciono el boton al formulario
        theTag.append(btn);
      } else if (tg === "form" && el.body && el.body.length > 0) {
        // si el tag es un form con elementos dentro
        // creo el formulario
        theTag = document.createElement("form");
        theTag.action = "#";
        theTag.className = "form-custom";
        // envio a botino un mensaje personalizado
        theTag.onsubmit = function () {
          return sendCustomMessage(this);
        };
        // recorro todos los elementos del body del formulario
        el.body.forEach(function (body_el) {
          // si el elemento del body tiene tag
          if (body_el.tag) {
            // creo el componente del formulario con el tag que envia el usuario
            var bTag = body_el.tag.toLowerCase();
            var comp = document.createElement(bTag);
            // recorro todas las properties del elemento
            Object.keys(body_el).forEach(function (k) {
              var subtag = k.toLowerCase();
              // si la propiedad no es tag
              if (subtag !== "tag" && subtag !== "body") {
                // si el elemento es img y la property es src
                if (bTag === "img" && subtag === "src") {
                  // le pongo que busque la imagen en imagesFolder
                  comp.src = imagesFolder + body_el[k];
                } else {
                  // le pongo la propiedad al elemento que estoy creando
                  comp[k] = body_el[k];
                }
              }
            });
            if (body_el.body && body_el.body.length > 0) {
              // pongo el body en el componente
              buildBody(body_el.body, comp, imagesFolder);
            }
            // adiciono el elemento al formulario
            theTag.append(comp);
          }
        });
        // adiciono siempre un boton submit para enviar el formulario personalizado a botino
        var btn = document.createElement("button");
        btn.type = "submit";
        btn.className = "btn";
        img = document.createElement("img");
        img.className = "icon-chat";
        img.src = imagesFolder + "send_msg.png";
        btn.append(img);
        theTag.append(btn);
      } else {
        // adiciono los otros elementos que envia botino
        theTag = document.createElement(tg);
        // recorro todas las propiedades del elemento
        Object.keys(el).forEach(function (k) {
          var subtag = k.toLowerCase();
          // si la propiedad no es tag
          if (subtag !== "tag" && subtag !== "body") {
            // si el elemento es img y la propiedad es src
            if (tg === "img" && subtag === "src") {
              // le pongo que busque la imagen en imagesFolder
              theTag.src = imagesFolder + el[k];
            } else {
              // adiciono la propiedad al elemento
              theTag[k] = el[k];
            }
          }
        });
        if (el.body && el.body.length > 0) {
          // pongo el body en la respuesta
          buildBody(el.body, theTag, imagesFolder);
        }
      }
      // adiciono el elemento a la etiqueta que se pasó a la función
      div_msg.append(theTag);
    }
  });
}
