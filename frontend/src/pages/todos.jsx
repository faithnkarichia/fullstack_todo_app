    
    import { useEffect, useState } from "react";
    export default function Todos(){
        const [tasks, setTasks] = useState([]);
        const [newTask, setNewTask] = useState('');
      
        const addTask = () => {
            const token=localStorage.getItem("access_token")
          
            fetch("http://localhost:5555/add_todo",{
                method:"POST",
                headers:{
                    "Content-Type":"Application/json",
                    Authorization: `Bearer ${token}`
                },
                body:JSON.stringify({
                    title: newTask.title,
                    description: newTask.description,
                  })
            })
            .then(res=>res.json())
            .then((data)=>{
                console.log("Task added:", data);
                setTasks((prev)=>[...prev,data])
                setNewTask({ title: "", description: "" });
            })

            

          
        };
      
        const toggleTaskCompletion = (index) => {
          const updatedTasks = tasks.map((task, i) =>
            i === index ? { ...task, completed: !task.completed } : task
          );
          setTasks(updatedTasks);
        };
      
        const deleteTask = (id) => {
            const token = localStorage.getItem("access_token");
          
            fetch(`http://localhost:5555/delete/${id}`, {
              method: "DELETE",
              headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${token}`,
              },
            })
              .then((res) => {
                if (!res.ok) {
                  throw new Error("Failed to delete task");
                }
                return res.json();
              })
              .then((data) => {
                console.log("Deleted:", data);
                // ✅ Remove task from UI
                setTasks((prev) => prev.filter((task) => task.id !== id));
              })
              .catch((err) => {
                console.error("Error deleting task:", err.message);
              });
          };
          


        // get users tasks
      useEffect(()=>{
        // get the acess token
        const token =localStorage.getItem("access_token")
        console.log(token)
        fetch("http://localhost:5555/todos",{
            headers:{
                "Content-Type":"Application/json",
                Authorization: `Bearer ${token}`
            }
        })
        .then( res=>res.json())
        .then((data)=>{
            console.log(data)
            setTasks(data)
        })

      },[])
      console.log(tasks)
      
        return (
          <div className="max-w-md mx-auto mt-10 p-4 bg-white rounded-lg shadow-lg">
            <h1 className="text-2xl font-bold mb-4">Todo List</h1>
            <div className="flex mb-4">
            <input
  type="text"
  className="flex-1 p-2 border rounded mb-2"
  value={newTask.title}
  onChange={(e) => setNewTask({ ...newTask, title: e.target.value })}
  placeholder="Title"
/>

<textarea
  className="flex-1 p-2 border rounded mb-2"
  value={newTask.description}
  onChange={(e) => setNewTask({ ...newTask, description: e.target.value })}
  placeholder="Description"
/>
              <button
                onClick={addTask}
                className="ml-2 p-2 bg-blue-500 text-white rounded hover:bg-blue-600"
              >
                Add
              </button>
            </div>
            <ul>
  {tasks.map((task, index) => (
    
    <li key={index} className="flex justify-between items-center mb-2 border p-2 rounded bg-white shadow">
      <span
        className={`flex-1 cursor-pointer text-lg ${task.completed ? 'line-through text-gray-500' : 'text-black'}`}
        onClick={() => toggleTaskCompletion(index)}
      >
        <strong>{task.title || "No title"}</strong><br />
        {task.description || "No text!"}
      </span>
      <button
        onClick={() => deleteTask(task.id)} 
        className="ml-4 px-3 py-1 bg-red-500 text-white rounded hover:bg-red-600"
      >
        Delete
      </button>
    </li>
  ))}
</ul>

          </div>
        );
    }