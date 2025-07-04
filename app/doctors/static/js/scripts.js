// nav bar
const swp = document.querySelector("#toggle-btn");

swp.addEventListener("click", function () {
  document.querySelector("#sidebar").classList.toggle("expand");
});

// help 
let helpOpen = false;
function toggleHelp() {
  const panel = document.getElementById('helpPanel');
  helpOpen = !helpOpen;
  if (helpOpen) {
    panel.style.opacity = '1';
    panel.style.transform = 'translateY(0)';
    panel.style.visibility = 'visible';
  } else {
    panel.style.opacity = '0';
    panel.style.transform = 'translateY(10px)';
    panel.style.visibility = 'hidden';
  }
}


// calendar
document.addEventListener('DOMContentLoaded', function () {
  const calendarEl = document.getElementById('calendar');

  const calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'timeGridWeek',  // You can use dayGridMonth, timeGridDay, etc.
    headerToolbar: {
      left: 'prev,next today',
      center: 'title',
      right: 'dayGridMonth,timeGridWeek,timeGridDay'
    },
    slotMinTime: "07:00:00",
    slotMaxTime: "18:00:00",
    allDaySlot: false,
    height: "auto",
    events: [
      {
        title: 'Dr. John Mensah - Room A',
        start: '2025-06-24T09:00:00',
        end: '2025-06-24T14:00:00',
        color: '#198754' // green
      },
      {
        title: 'Nurse Akosua - Ward B',
        start: '2025-06-25T10:00:00',
        end: '2025-06-25T13:00:00',
        color: '#0d6efd' // blue
      },
      {
        title: 'Dr. Efua Asante - Room C',
        start: '2025-06-26T11:00:00',
        end: '2025-06-26T15:00:00',
        color: '#ffc107' // yellow
      }
    ]
  });

  calendar.render();
});


// profile inputs toggle
function togglePassword(fieldId, icon) {
  const input = document.getElementById(fieldId);
  if (input.type === 'password') {
    input.type = 'text';
    icon.classList.remove('bi-eye-slash');
    icon.classList.add('bi-eye');
  } else {
    input.type = 'password';
    icon.classList.remove('bi-eye');
    icon.classList.add('bi-eye-slash');
  }
}


// notifications
function openNotification(message) {
  document.getElementById('notificationContent').innerText = message;
  document.getElementById('notificationModal').classList.add('show');
  document.getElementById('overlay').classList.add('show');
}

function closeNotification() {
  document.getElementById('notificationModal').classList.remove('show');
  document.getElementById('overlay').classList.remove('show');
}


// Help 
  function toggleHelp(show) {
    document.getElementById('helpSidebar').classList.toggle('show', show);
    document.getElementById('helpOverlay').classList.toggle('show', show);
  }