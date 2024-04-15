package com.example.sportapp.ui.views

import android.content.Context
import android.content.Intent
import android.icu.text.SimpleDateFormat
import android.os.Bundle
import android.os.SystemClock
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.Chronometer
import android.widget.ImageView
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.example.sportapp.R
import com.example.sportapp.SportApp
import com.example.sportapp.data.model.StartTrainingResponse
import com.example.sportapp.data.repository.StartTrainingRepository
import com.example.sportapp.data.services.RetrofitStartTrainingService
import com.example.sportapp.ui.home.Home
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response


class StartTraining : AppCompatActivity() {


    private val repository = StartTrainingRepository(RetrofitStartTrainingService.createApiService())
    private lateinit var chronometer: Chronometer

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_start_training)

        val ivRunExe = findViewById<ImageView>(R.id.ivRunExe)
        val ivHome = findViewById<ImageView>(R.id.ivHome)
        val btnIniciar = findViewById<Button>(R.id.btnStartTraining)


        btnIniciar.setOnClickListener{
            val runTra = Intent(this, RunTraining::class.java)
            runTra.putExtra("training", "Running")
            startActivity(runTra)
        }

        ivHome.setOnClickListener{
            val home = Intent(this, Home::class.java)
            startActivity(home)
        }

        ivRunExe.setOnClickListener{
            val startTra = Intent(this, StartTraining::class.java)
            startActivity(startTra)
        }


        /*Conectar con servicio iniciar entrenamiento*/
        repository.startTrainingService(1, "Cardio", object : Callback<StartTrainingResponse> {
            override fun onResponse(call: Call<StartTrainingResponse>, response: Response<StartTrainingResponse>) {
                if (response.isSuccessful) {
                    val startTrainingResponse = response.body()
                    SportApp.userSesionId = startTrainingResponse?.session_id.toString()
                    showToast(this@StartTraining, getString(R.string.promt_start_training))
                    Log.d("DEBUG", "Sesion Id : " + SportApp.userSesionId)
                } else {
                    val errorMessage = "La llamada al servicio no fue exitosa. Código de error: ${response.code()}"
                    showToast(this@StartTraining, errorMessage)
                    Log.d("DEBUG", errorMessage)
                }
            }

            override fun onFailure(call: Call<StartTrainingResponse>, t: Throwable) {
                // Manejar errores de red o de llamada al servicio
                Log.d("DEBUG", "Error en la llamada al servicio: ${t.message}")
                t.printStackTrace()
            }
        })

        //Inicializa datos de entrenamiento.
        val dataList = listOf("Natacion", "Ciclismo", "Running") // Lista de datos
        val recyclerView = findViewById<RecyclerView>(R.id.rvTypeTraining)
        recyclerView.layoutManager = LinearLayoutManager(this)
        recyclerView.adapter = MyAdapter(dataList)
        chronometer = findViewById(R.id.chronometer)

    }

    private class MyAdapter(private val dataList: List<String>) : RecyclerView.Adapter<MyAdapter.ViewHolder>() {

        override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
            val view = LayoutInflater.from(parent.context).inflate(R.layout.item_layout, parent, false)
            return ViewHolder(view)
        }

        override fun onBindViewHolder(holder: ViewHolder, position: Int) {
            val item = dataList[position]
            holder.textViewItem.text = item

        }

        override fun getItemCount(): Int {
            return dataList.size
        }

        inner class ViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
            val textViewItem: TextView = itemView.findViewById(R.id.textViewItem)
        }
    }

    fun showToast(context: Context, message: String, duration: Int = Toast.LENGTH_SHORT) {
        Toast.makeText(context, message, duration).show()
    }
}
