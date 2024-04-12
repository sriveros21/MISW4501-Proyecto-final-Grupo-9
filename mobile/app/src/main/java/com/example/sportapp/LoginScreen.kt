package com.example.sportapp
import android.content.Intent
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.lifecycleScope
import com.android.volley.toolbox.HttpResponse
import com.example.sportapp.data.api.ApiService
import com.example.sportapp.data.api.EventsService
import com.example.sportapp.data.model.CalendarEvent
import com.example.sportapp.ui.home.Home
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking
import kotlinx.coroutines.withContext
import okhttp3.OkHttpClient
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import java.io.IOException
import okhttp3.Request
import kotlin.math.log

//import io.ktor.client.HttpClient
//import io.ktor.client.engine.android.Android
//import io.ktor.client.request.get
//import io.ktor.client.statement.HttpResponse
//import kotlinx.coroutines.Dispatchers
//import kotlinx.coroutines.withContext

class LoginScreen : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)
        // String appName = getString(R.string.app_name)

        val btnLoginE = findViewById<Button>(R.id.btnLogin)


        //Redirige a la Actividad Home.
        btnLoginE.setOnClickListener{
            val home = Intent(this, Home::class.java)
            startActivity(home)
        }


//        // Configurar Retrofit
//        val retrofit = Retrofit.Builder()
//            .baseUrl("http://localhost:3002/")
//            .addConverterFactory(GsonConverterFactory.create())
//            .build()
//
//        // Crear una instancia de la interfaz de servicio
//        val apiService = retrofit.create(ApiService::class.java)
//
//        Log.d("DEBUG", "La llamada al servicio no fue exitosa. Código de error: ${apiService.toString()}")
//
//        // Realizar la solicitud
//        val call = apiService.getCalendarEvents(1)
//
//
//        // Enqueue la solicitud en un hilo en segundo plano
//        // Ejecutar la llamada asíncronamente
//        call.enqueue(object : Callback<List<CalendarEvent>> {
//            override fun onResponse(call: Call<List<CalendarEvent>>, response: Response<List<CalendarEvent>>) {
//                if (response.isSuccessful) {
//                    // Si la llamada es exitosa, procesar la respuesta
//
//                    val datos = response.body()
//                    // Toast.makeText(this@LoginScreen, "Datos recibidos: $datos", Toast.LENGTH_SHORT).show()
//
//                    Log.d("DEBUG", "EXITOSA. Código de error: ${response.code()}")
//
//                } else {
//                    // Si la llamada no es exitosa, manejar el error
//                    //Toast.makeText(this@LoginScreen, "Error en la llamada: ${response.message()}", Toast.LENGTH_SHORT).show()
//
//                    Log.d("DEBUG", "La llamada al servicio no fue exitosa. Código de error: ${response.code()}")
//                }
//            }

//            override fun onFailure(call: Call<List<CalendarEvent>>, t: Throwable) {
//                // Manejar el error en caso de que falle la llamada
//                //Toast.makeText(this@LoginScreen, "Error de conexión: ${t.message}", Toast.LENGTH_SHORT).show()
//                Log.d("DEBUG", "LOG ERROR. Código de error: ${t.message}")
//
//            }
//        })


//        /*  KTOR */
//        val client = HttpClient(Apache)
//
//        // Define la URL del servicio al que deseas hacer la solicitud
//        val url = "https://api.example.com/data"
//
//        // Utiliza runBlocking para ejecutar una operación suspendida de manera síncrona
//        runBlocking {
//            // Realiza una solicitud GET al servicio y almacena la respuesta en una variable
//            val response: HttpResponse = client.get(url)
//
//            // Imprime el código de estado de la respuesta
//            println("Código de estado: ${response.status.value}")
//
//            // Lee el cuerpo de la respuesta como una cadena y lo imprime
//            val responseBody: String = response.readText()
//            println("Cuerpo de la respuesta: $responseBody")
//        }
//
//        // Cierra el cliente HTTP cuando hayas terminado de usarlo
//        client.close()


        /**/
//        val client = OkHttpClient()
//
//        val url = "http://127.0.0.1:3002/user/1/calendar"
//        val request = Request.Builder()
//            .url(url)
//            .build()
//
//        try {
//            val response: okhttp3.Response = client.newCall(request).execute()
//            if (response.isSuccessful) {
//                val responseData = response.body?.string()
//                println(" OK Respuesta del servidor: $responseData")
//            } else {
//                println("ERRROR  Error en la solicitud: ${response.code}")
//            }
//        } catch (e: IOException) {
//            println("Error al realizar la solicitud: ${e.message}")
//        }

//        lifecycleScope.launch {
//            getDataFromService()
//        }

    }

//    suspend fun getDataFromService() {
//        val responseData = withContext(Dispatchers.IO) {
//            fetchDataFromService()
//        }
//        Log.d("DEBUG", "LOG ERROR. Código de error: ${responseData.toString()}")
//
//    }

//    suspend fun fetchDataFromService(): String? {
//        val client = OkHttpClient()
//        val request = Request.Builder()
//            .url("http://192.168.25.114:3002/user/1/calendar")
//            .build()
//
//        return try {
//            val response: okhttp3.Response = client.newCall(request).execute()
//            if (response.isSuccessful) {
//                response.body?.string()
//
//            } else {
//                null // Manejar errores de solicitud aquí
//
//            }
//        } catch (e: IOException) {
//            e.printStackTrace()
//            null // Manejar errores de red aquí
//        }
//    }
}
