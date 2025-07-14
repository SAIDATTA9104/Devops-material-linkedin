package com.moviemagic;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.client.RestTemplate;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;

@Controller
public class MovieController {
    
    @Value("${backend.url}")
    private String backendUrl;

    @GetMapping("/")
    public String index(Model model) {
        return "index";
    }

    @PostMapping("/search")
    public String searchMovie(@RequestParam String title, Model model) {
        try {
            RestTemplate restTemplate = new RestTemplate();
            String url = backendUrl + "/api/movies?title=" + 
                         URLEncoder.encode(title, StandardCharsets.UTF_8.toString());
            String result = restTemplate.getForObject(url, String.class);
            model.addAttribute("result", result);
        } catch (Exception e) {
            model.addAttribute("result", "Error: " + e.getMessage());
        }
        return "index";
    }
}