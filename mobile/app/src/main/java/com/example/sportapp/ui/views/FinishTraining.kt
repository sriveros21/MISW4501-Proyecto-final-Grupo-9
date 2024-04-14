package com.example.sportapp.ui.views

import android.content.Context
import android.content.Intent
import android.icu.text.SimpleDateFormat
import android.os.Bundle
import android.util.Log
import android.widget.ImageView
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.example.sportapp.R
import com.example.sportapp.data.model.TrainingMetricsCalculatedResponse
import com.example.sportapp.data.repository.FTPVO2Repository
import com.example.sportapp.data.services.RetrofitCalculateFTPVO2max
import com.example.sportapp.ui.home.Home
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import java.util.Date
import java.util.Locale

class FinishTraining : AppCompatActivity() {

    private val repository = FTPVO2Repository(RetrofitCalculateFTPVO2max.createApiService())
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_finish_training)

        val ivHome = findViewById<ImageView>(R.id.ivHome)
        val ivRunExe = findViewById<ImageView>(R.id.ivRunExe)

        //Variables de la vista
        val tvwTypeRun = findViewById<TextView>(R.id.tvwType)
        val tvwTimeTotal = findViewById<TextView>(R.id.tvwTimeTotal)
        val tvwDateTraining = findViewById<TextView>(R.id.tvwDateTraining)
        val tvwCalTraining = findViewById<TextView>(R.id.tvwCalTraining)
        val tvwFTP = findViewById<TextView>(R.id.tvwFTP)
        val tvwVO2 = findViewById<TextView>(R.id.tvwVO2)

        ivHome.setOnClickListener{
            val home = Intent(this, Home::class.java)
            startActivity(home)
        }

        ivRunExe.setOnClickListener{
            val home = Intent(this, StartTraining::class.java)
            startActivity(home)
        }


        val timeTraining = intent.getStringExtra("timeTraining").toString()
        val valorTraining = intent.getStringExtra("valorTraining").toString()

        repository.postCalculateFTPVo2(1, object : Callback<TrainingMetricsCalculatedResponse> {
            override fun onResponse(call: Call<TrainingMetricsCalculatedResponse>, response: Response<TrainingMetricsCalculatedResponse>) {
                if (response.isSuccessful) {
                    val metricsResponse = response.body()
                    // Acceder a los datos en la respuesta y hacer lo que necesites hacer con ellos
                    metricsResponse?.let { metrics ->
                        val session_id = metrics.data.session_id
                        val user_id = metrics.data.user_id
                        val ftp = metrics.data.ftp
                        val vo2max = metrics.data.vo2max
                        val timestamp = metrics.data.timestamp

                        tvwTypeRun.text = tvwTypeRun.text.toString() + " " +  valorTraining
                        tvwTimeTotal.text = tvwTimeTotal.text.toString() + " " + timeTraining
                        tvwDateTraining.text = tvwDateTraining.text.toString() + " " + SimpleDateFormat("dd/MM/yyyy", Locale.getDefault()).format(Date())
                        tvwCalTraining.text = tvwCalTraining.text.toString() + " " + "500 kCal"
                        tvwFTP.text = tvwFTP.text.toString() + " " + ftp //"238 vatios"
                        tvwVO2.text = tvwVO2.text.toString() + " " + vo2max //"60 ml/kg/min"

                    }
                } else {
                    val errorMessage = "La llamada al servicio no fue exitosa. Código de error: ${response.code()}"
                    // Manejar la respuesta de error aquí
                    showToast(this@FinishTraining, errorMessage)
                    Log.d("DEBUG", errorMessage)
                }
            }

            override fun onFailure(call: Call<TrainingMetricsCalculatedResponse>, t: Throwable) {
                // Manejar errores de red o de llamada al servicio
                Log.d("DEBUG", "Error en la llamada al servicio: ${t.message}")
                t.printStackTrace()
            }
        })
    }

    fun showToast(context: Context, message: String, duration: Int = Toast.LENGTH_SHORT) {
        Toast.makeText(context, message, duration).show()
    }
}