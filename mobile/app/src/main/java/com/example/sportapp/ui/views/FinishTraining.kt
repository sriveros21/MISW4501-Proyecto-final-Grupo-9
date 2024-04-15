package com.example.sportapp.ui.views

import android.content.Context
import android.content.Intent
import android.icu.text.SimpleDateFormat
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.ImageView
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.example.sportapp.R
import com.example.sportapp.SportApp
import com.example.sportapp.data.model.ReceiveSesionDataResponse
import com.example.sportapp.data.model.StopTrainingResponse
import com.example.sportapp.data.model.TrainingMetricsCalculatedResponse
import com.example.sportapp.data.repository.FTPVO2Repository
import com.example.sportapp.data.repository.ReceiveSesionDataRepository
import com.example.sportapp.data.repository.StopTrainingRepository
import com.example.sportapp.data.services.RetrofitCalculateFTPVO2max
import com.example.sportapp.data.services.RetrofitReceiveSesionDataService
import com.example.sportapp.data.services.RetrofitStopTrainingService
import com.example.sportapp.ui.home.Home
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import java.util.Date
import java.util.Locale

class FinishTraining : AppCompatActivity() {


    private val repositoryStop = StopTrainingRepository(RetrofitStopTrainingService.createApiService())
    private val repositoryReceiveData = ReceiveSesionDataRepository(RetrofitReceiveSesionDataService.createApiService())
    private val repository = FTPVO2Repository(RetrofitCalculateFTPVO2max.createApiService())

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_finish_training)

        val ivHome = findViewById<ImageView>(R.id.ivHome)
        val ivRunExe = findViewById<ImageView>(R.id.ivRunExe)
        val btnFTPVO2 = findViewById<Button>(R.id.btnStart)

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

        btnFTPVO2.setOnClickListener{
            //val home = Intent(this, StartTraining::class.java)
            //startActivity(home)
            //FTP
            repository.postCalculateFTPVo2(SportApp.userSesionId, object : Callback<TrainingMetricsCalculatedResponse> {
                override fun onResponse(call: Call<TrainingMetricsCalculatedResponse>, response: Response<TrainingMetricsCalculatedResponse>) {
                    if (response.isSuccessful) {
                        //val metricsResponse = response.body()
                        val metricsResponse = response.body()

                        Log.d("DEBUG",  "Body > " + response.body().toString() + " Sesion -> " + SportApp.userSesionId)

                        tvwFTP.text = tvwFTP.text.toString() + " " + metricsResponse?.ftp.toString() //"238 vatios"
                        tvwVO2.text = tvwVO2.text.toString() + " " + metricsResponse?.vo2max.toString() //"60 ml/kg/min"

                        showToast(this@FinishTraining, "Calculo FTp y VO2Max Exitoso!!")
                        val Message = "Valores generados FTP : > " +  metricsResponse?.ftp.toString() + " Vo2 > " + metricsResponse?.vo2max.toString()
                        Log.d("DEBUG", Message)
                        Log.d("DEBUG", metricsResponse.toString())

                    } else {
                        val errorMessage = "Error en la llamada al servicio FTPVo2Max . Código de error: ${response.code()}"
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

        var timeTraining = intent.getIntExtra("timeTraining",0)
        val typeTraining = intent.getStringExtra("typeTraining")
        val caloriesBurned = intent.getIntExtra("caloriesBurned", 0)

        repositoryStop.stopTrainingService(SportApp.userSesionId, Date(), timeTraining.toInt(), caloriesBurned, "", object : Callback<StopTrainingResponse> {
            override fun onResponse(call: Call<StopTrainingResponse>, response: Response<StopTrainingResponse>) {
                if (response.isSuccessful) {
                    //val stopTrainingResponse = response.body()
                    //SportApp.userSesionId = stopTrainingResponse?.session_id.toString()

                    tvwTypeRun.text = tvwTypeRun.text.toString() + " " +  typeTraining
                    tvwTimeTotal.text = tvwTimeTotal.text.toString() + " " + timeTraining.toString() + " " + getString(R.string.units_minutes)
                    tvwDateTraining.text = tvwDateTraining.text.toString() + " " + SimpleDateFormat("dd/MM/yyyy", Locale.getDefault()).format(Date())
                    tvwCalTraining.text = tvwCalTraining.text.toString() + " " + caloriesBurned

                    showToast(this@FinishTraining, getString(R.string.promt_finish_training))
                    Log.d("DEBUG", "Sesion Finalizada Correctamente : " + SportApp.userSesionId)

                } else {
                    val errorMessage = "Error al finalizar sesion. Código de error: ${response.code()}"
                    showToast(this@FinishTraining, errorMessage)
                    Log.d("DEBUG", errorMessage)
                }

                //Receive
                repositoryReceiveData.receiveSesionDataService(SportApp.userSesionId, SportApp.powerOutput, SportApp.maxHeartRate, SportApp.restingHeartRate, object : Callback<ReceiveSesionDataResponse> {
                    override fun onResponse(call: Call<ReceiveSesionDataResponse>, response: Response<ReceiveSesionDataResponse>) {
                        if (response.isSuccessful) {
                            val receiveDataSesionResponse = response.body()

                            showToast(this@FinishTraining, getString(R.string.promt_data_sended))
                            Log.d("DEBUG", "Receive data sesion exitosa : " + receiveDataSesionResponse?.message.toString())

                        } else {
                            val errorMessage = "Error al llamar servicio Receive Sesion Data . Código de error: ${response.code()}"
                            showToast(this@FinishTraining, errorMessage)
                            Log.d("DEBUG", errorMessage)
                        }



                    }

                    override fun onFailure(call: Call<ReceiveSesionDataResponse>, t: Throwable) {
                        // Manejar errores de red o de llamada al servicio
                        Log.d("DEBUG", "Error en la llamada al servicio: ${t.message}")
                        t.printStackTrace()
                    }
                })



            }

            override fun onFailure(call: Call<StopTrainingResponse>, t: Throwable) {
                // Manejar errores de red o de llamada al servicio
                Log.d("DEBUG", "Error al finalizar sesion service.: ${t.message}")
                t.printStackTrace()
            }
        })

    }

    fun showToast(context: Context, message: String, duration: Int = Toast.LENGTH_SHORT) {
        Toast.makeText(context, message, duration).show()
    }
}