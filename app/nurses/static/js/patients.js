const toggleBtn = document.getElementById('toggleEditBtn');
const textareas = document.querySelectorAll('textarea.readonly-textarea');
let editMode = false;
toggleBtn.addEventListener('click', () => {
    editMode = !editMode;
    textareas.forEach(box => {
        box.readOnly = !editMode;
        box.classList.toggle('bg-white', editMode);
    });

    toggleBtn.innerHTML = editMode
        ? '<i class="bi bi-eye me-1"></i> View Mode'
        : '<i class="bi bi-pencil-square me-1"></i> Edit Record';
});

function exportPDF() {
    const originalActiveTab = document.querySelector('.tab-pane.active');
    const allTabs = document.querySelectorAll('.tab-pane');
    const labTab = document.getElementById('lab');
    const buttons = document.querySelectorAll('.no-print');
    const tableHeaders = document.querySelectorAll('thead');

    // Temporarily show all tabs except lab
    allTabs.forEach(tab => {
        if (tab.id !== 'lab') {
            tab.classList.add('show', 'active');
        }
    });

    // Hide buttons and table headers for export
    buttons.forEach(btn => btn.style.display = 'none');
    tableHeaders.forEach(th => th.style.display = 'none');

    html2pdf()
        .from(document.getElementById('recordContainer'))
        .set({
            margin: [0.5, 0.75],
            filename: 'patient-medical-record.pdf',
            html2canvas: { scale: 2 },
            jsPDF: { unit: 'in', format: 'letter', orientation: 'portrait' }
        })
        .save()
        .then(() => {
            // Revert visibility
            buttons.forEach(btn => btn.style.display = '');
            tableHeaders.forEach(th => th.style.display = '');
            allTabs.forEach(tab => tab.classList.remove('show', 'active'));
            if (originalActiveTab) originalActiveTab.classList.add('show', 'active');
        });
}