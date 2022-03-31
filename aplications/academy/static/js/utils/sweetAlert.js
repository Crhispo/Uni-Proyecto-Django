const swalnote = (Icon, Title, Tex, cBT) => {
    Swal.fire({
        icon: Icon,
        title: Title,
        text: Tex,
        confirmButtonText: cBT,
    });
}

const swalchoices = (Icon, Title, Tex, cBT, event) => {
    Swal.fire({
        icon: Icon,
        title: Title,
        text: Tex,
        confirmButtonText: cBT,
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Confirmar',
        cancelButtonText: 'Cancelar',
        preConfirm: () => {
            location.href = event.target.href
        },
    })
}