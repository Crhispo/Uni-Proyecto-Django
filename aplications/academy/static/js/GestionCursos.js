document.addEventListener("DOMContentLoaded", function (event) {
    const $FormRegistroCursos = document.getElementById('FormRegistroCursos');
    const $txtNombre = document.getElementById('txtNombre');
    const $btn_delete = document.querySelectorAll('.btn-delete');
    (function () {
        $FormRegistroCursos.addEventListener('submit',
            function (event) {
                let nombre = String($txtNombre.value).trim();
                if (nombre.length == 0) {
                    swalnote('warning', document.title, 'El nombre del curso no puede estar vacio...', 'Entendido');
                    event.preventDefault();
                }
            }
        )

        $btn_delete.forEach(btn => {
            btn.addEventListener('click', function (event) {
                event.preventDefault()
                swalchoices('warning', document.title, '¿Desea eliminar el curso?', true, event)
            })

        })

    })()
})