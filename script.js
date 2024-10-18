function loadTasks() {
    let tasks = localStorage.getItem('tasks');
    return tasks ? JSON.parse(tasks) : [];
}

function saveTasks(tasks) {
    localStorage.setItem('tasks', JSON.stringify(tasks));
}

function renderTasks() {
    const taskList = document.getElementById('tasks');
    taskList.innerHTML = '';
    const tasks = loadTasks();

    tasks.forEach((task, index) => {
        const taskItem = document.createElement('li');
        taskItem.className = task.completed ? 'completed' : '';

        taskItem.innerHTML = `
            <span>${task.title} - ${task.description} [${task.category}]</span>
            <div>
                <button class="complete" onclick="toggleComplete(${index})">Complete</button>
                <button class="edit" onclick="editTask(${index})">Edit</button>
                <button class="delete" onclick="deleteTask(${index})">Delete</button>
            </div>
        `;
        taskList.appendChild(taskItem);
    });
}

function addTask() {
    const title = document.getElementById('task-title').value;
    const desc = document.getElementById('task-desc').value;
    const category = document.getElementById('task-category').value;

    if (title === '' || desc === '') {
        alert('Please fill in both title and description.');
        return;
    }

    const tasks = loadTasks();
    const newTask = {
        title: title,
        description: desc,
        category: category,
        completed: false
    };

    tasks.push(newTask);
    saveTasks(tasks); 
    renderTasks();
    clearForm();
}

function toggleComplete(index) {
    const tasks = loadTasks();
    tasks[index].completed = !tasks[index].completed;
    saveTasks(tasks);
    renderTasks();
}

function deleteTask(index) {
    const tasks = loadTasks();
    tasks.splice(index, 1);
    saveTasks(tasks);
    renderTasks();
}

function editTask(index) {
    const tasks = loadTasks();
    const task = tasks[index];

    document.getElementById('task-title').value = task.title;
    document.getElementById('task-desc').value = task.description;
    document.getElementById('task-category').value = task.category;

    deleteTask(index); 
}

function clearForm() {
    document.getElementById('task-title').value = '';
    document.getElementById('task-desc').value = '';
    document.getElementById('task-category').value = 'Work';
}

document.getElementById('add-task-btn').addEventListener('click', addTask);

renderTasks();
