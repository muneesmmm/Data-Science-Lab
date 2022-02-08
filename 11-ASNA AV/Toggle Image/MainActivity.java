package com.example.toggles;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.FrameLayout;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {
    ImageView i1, i2;
    Button b1;
    FrameLayout f1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        i1 = (ImageView) findViewById(R.id.ImageView1);
        i2 = (ImageView) findViewById(R.id.ImageView2);
        b1=(Button) findViewById(R.id.button);
        i1.setOnClickListener(this);
        i2.setOnClickListener(this);
        b1.setOnClickListener(this);
        f1=(FrameLayout) findViewById(R.id.f1);

    }

    @Override
    public void onClick(View v) {
        if (v.getId() == R.id.ImageView1) {
            i1.setVisibility(View.GONE);
            i2.setVisibility(View.VISIBLE);
        } else {
            i2.setVisibility(View.GONE);
            i1.setVisibility(View.VISIBLE);
        }
        if(v.getId()==R.id.button){
            f1.setBackgroundColor(getResources().getColor(R.color.purple_500));
        }

    }
}

