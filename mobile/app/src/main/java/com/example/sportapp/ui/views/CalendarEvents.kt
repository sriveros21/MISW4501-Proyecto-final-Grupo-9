package com.example.sportapp.ui.views

import android.content.Intent
import android.os.Bundle
import android.view.LayoutInflater
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.sportapp.R
import com.example.sportapp.ui.home.Home
import androidx.recyclerview.widget.RecyclerView
import android.view.View

class CalendarEvents : AppCompatActivity() {

    private lateinit var tableAdapter: TableAdapter
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_calendar_events)

        val ivHome = findViewById<ImageView>(R.id.ivHome)
        val ivRunExe = findViewById<ImageView>(R.id.ivRunExe)

        ivHome.setOnClickListener{
            val home = Intent(this, Home::class.java)
            startActivity(home)
        }

        ivRunExe.setOnClickListener{
            val home = Intent(this, StartTraining::class.java)
            startActivity(home)
        }


        //Tabla de eventos
        val recyclerView = findViewById<RecyclerView>(R.id.rvEvents)
        recyclerView.layoutManager = LinearLayoutManager(this)

        tableAdapter = TableAdapter(mutableListOf())
        recyclerView.adapter = tableAdapter

        /* Conectar con servicio y traer datos. */


        // Agregar datos de ejemplo.
        val data = listOf(
            Triple("Evento 1", "2010-01-01", "Descripcion del evento 1"),
            Triple("Evento 2", "2010-01-02", "Descripcion del evento 2"),
            Triple("Evento 3", "2010-01-03", "Descripcion del evento 3"),
            // Agregar más datos si es necesario
        )
        data.forEach { tableAdapter.addItem(it) }

    }


    class TableAdapter(private val data: MutableList<Triple<String, String, String>>) :
        RecyclerView.Adapter<TableAdapter.ViewHolder>() {

        override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
            val view = LayoutInflater.from(parent.context).inflate(R.layout.item_layout_event, parent, false)
            return ViewHolder(view)
        }

        override fun onBindViewHolder(holder: ViewHolder, position: Int) {
            val item = data[position]
            holder.column1TextView.text = item.first
            holder.column2TextView.text = item.second
            holder.column3TextView.text = item.third
        }

        override fun getItemCount(): Int {
            return data.size
        }

        fun addItem(item: Triple<String, String, String>) {
            data.add(item)
            notifyItemInserted(data.size - 1)
        }

        class ViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
            val column1TextView: TextView = itemView.findViewById(R.id.textViewColumn1)
            val column2TextView: TextView = itemView.findViewById(R.id.textViewColumn2)
            val column3TextView: TextView = itemView.findViewById(R.id.textViewColumn3)
        }
    }

}