def findDecision(obj): #obj[0]: protocol_type, obj[1]: service, obj[2]: flag, obj[3]: src_bytes, obj[4]: count, obj[5]: serror_rate, obj[6]: diff_srv_rate, obj[7]: dst_host_count, obj[8]: dst_host_srv_count, obj[9]: dst_host_same_srv_rate, obj[10]: dst_host_diff_srv_rate, obj[11]: dst_host_same_src_port_rate, obj[12]: dst_host_srv_diff_host_rate, obj[13]: dst_host_serror_rate, obj[14]: dst_host_rerror_rate
   # {"feature": "dst_host_serror_rate", "instances": 125973, "metric_value": 1.3913, "depth": 1}
   if obj[13]<=0.7292347469535909:
      # {"feature": "dst_host_srv_diff_host_rate", "instances": 90952, "metric_value": 1.1587, "depth": 2}
      if obj[12]<=0.37023252388068995:
         # {"feature": "dst_host_rerror_rate", "instances": 87290, "metric_value": 1.087, "depth": 3}
         if obj[14]<=0.11883181316631937:
            # {"feature": "protocol_type", "instances": 70018, "metric_value": 0.6437, "depth": 4}
            if obj[0]>0:
               # {"feature": "dst_host_same_src_port_rate", "instances": 64858, "metric_value": 0.3986, "depth": 5}
               if obj[11]<=0.7663706668194779:
                  # {"feature": "src_bytes", "instances": 59873, "metric_value": 0.2778, "depth": 6}
                  if obj[3]>0:
                     # {"feature": "flag", "instances": 58930, "metric_value": 0.2445, "depth": 7}
                     if obj[2]>6.97999571336715:
                        # {"feature": "dst_host_srv_count", "instances": 58475, "metric_value": 0.237, "depth": 8}
                        if obj[8]>115.65300500900987:
                           # {"feature": "dst_host_same_srv_rate", "instances": 46642, "metric_value": 0.0947, "depth": 9}
                           if obj[9]>0.5212416946488446:
                              # {"feature": "count", "instances": 45635, "metric_value": 0.088, "depth": 10}
                              if obj[4]<=84.1075547934875:
                                 # {"feature": "diff_srv_rate", "instances": 41022, "metric_value": 0.0961, "depth": 11}
                                 if obj[6]<=0.0:
                                    # {"feature": "service", "instances": 40246, "metric_value": 0.0963, "depth": 12}
                                    if obj[1]<=31.22646916402721:
                                       # {"feature": "dst_host_count", "instances": 36240, "metric_value": 0.1049, "depth": 13}
                                       if obj[7]<=182.14894461511594:
                                          # {"feature": "serror_rate", "instances": 18916, "metric_value": 0.0577, "depth": 14}
                                          if obj[5]<=0.7309383846979811:
                                             # {"feature": "dst_host_diff_srv_rate", "instances": 18882, "metric_value": 0.0578, "depth": 15}
                                             if obj[10]<=0.6497142587290661:
                                                return 'normal'
                                             elif obj[10]>0.6497142587290661:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          elif obj[5]>0.7309383846979811:
                                             return 'normal'
                                          else:
                                             return 'normal'
                                       elif obj[7]>182.14894461511594:
                                          # {"feature": "serror_rate", "instances": 17324, "metric_value": 0.1503, "depth": 14}
                                          if obj[5]<=0.7309383846979811:
                                             # {"feature": "dst_host_diff_srv_rate", "instances": 17308, "metric_value": 0.1504, "depth": 15}
                                             if obj[10]<=0.6497142587290661:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          elif obj[5]>0.7309383846979811:
                                             return 'normal'
                                          else:
                                             return 'normal'
                                       else:
                                          return 'normal'
                                    elif obj[1]>31.22646916402721:
                                       return 'normal'
                                    else:
                                       return 'normal'
                                 elif obj[6]>0.0:
                                    # {"feature": "service", "instances": 776, "metric_value": 0.0508, "depth": 12}
                                    if obj[1]>31.22646916402721:
                                       # {"feature": "dst_host_count", "instances": 440, "metric_value": 0.0232, "depth": 13}
                                       if obj[7]>182.14894461511594:
                                          return 'normal'
                                       elif obj[7]<=182.14894461511594:
                                          # {"feature": "serror_rate", "instances": 77, "metric_value": 0.1, "depth": 14}
                                          if obj[5]<=0.7309383846979811:
                                             # {"feature": "dst_host_diff_srv_rate", "instances": 76, "metric_value": 0.1011, "depth": 15}
                                             if obj[10]<=0.6497142587290661:
                                                return 'normal'
                                             elif obj[10]>0.6497142587290661:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          elif obj[5]>0.7309383846979811:
                                             return 'normal'
                                          else:
                                             return 'normal'
                                       else:
                                          return 'normal'
                                    elif obj[1]<=31.22646916402721:
                                       # {"feature": "dst_host_count", "instances": 336, "metric_value": 0.0818, "depth": 13}
                                       if obj[7]>182.14894461511594:
                                          # {"feature": "serror_rate", "instances": 320, "metric_value": 0.0852, "depth": 14}
                                          if obj[5]<=0.7309383846979811:
                                             # {"feature": "dst_host_diff_srv_rate", "instances": 320, "metric_value": 0.0852, "depth": 15}
                                             if obj[10]<=0.6497142587290661:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          else:
                                             return 'normal'
                                       elif obj[7]<=182.14894461511594:
                                          return 'normal'
                                       else:
                                          return 'normal'
                                    else:
                                       return 'normal'
                                 else:
                                    return 'normal'
                              elif obj[4]>84.1075547934875:
                                 return 'normal'
                              else:
                                 return 'normal'
                           elif obj[9]<=0.5212416946488446:
                              # {"feature": "service", "instances": 1007, "metric_value": 0.2337, "depth": 10}
                              if obj[1]>31.22646916402721:
                                 # {"feature": "diff_srv_rate", "instances": 781, "metric_value": 0.0141, "depth": 11}
                                 if obj[6]<=0.0:
                                    return 'normal'
                                 elif obj[6]>0.0:
                                    # {"feature": "dst_host_count", "instances": 45, "metric_value": 0.1537, "depth": 12}
                                    if obj[7]<=182.14894461511594:
                                       # {"feature": "count", "instances": 31, "metric_value": 0.2056, "depth": 13}
                                       if obj[4]<=84.1075547934875:
                                          # {"feature": "serror_rate", "instances": 31, "metric_value": 0.2056, "depth": 14}
                                          if obj[5]<=0.7309383846979811:
                                             # {"feature": "dst_host_diff_srv_rate", "instances": 31, "metric_value": 0.2056, "depth": 15}
                                             if obj[10]<=0.6497142587290661:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          else:
                                             return 'normal'
                                       else:
                                          return 'normal'
                                    elif obj[7]>182.14894461511594:
                                       return 'normal'
                                    else:
                                       return 'normal'
                                 else:
                                    return 'normal'
                              elif obj[1]<=31.22646916402721:
                                 # {"feature": "dst_host_count", "instances": 226, "metric_value": 0.6326, "depth": 11}
                                 if obj[7]>182.14894461511594:
                                    # {"feature": "count", "instances": 178, "metric_value": 0.7264, "depth": 12}
                                    if obj[4]<=84.1075547934875:
                                       # {"feature": "serror_rate", "instances": 178, "metric_value": 0.7264, "depth": 13}
                                       if obj[5]<=0.7309383846979811:
                                          # {"feature": "diff_srv_rate", "instances": 178, "metric_value": 0.7264, "depth": 14}
                                          if obj[6]<=0.0:
                                             # {"feature": "dst_host_diff_srv_rate", "instances": 178, "metric_value": 0.7264, "depth": 15}
                                             if obj[10]<=0.6497142587290661:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          else:
                                             return 'normal'
                                       else:
                                          return 'normal'
                                    else:
                                       return 'normal'
                                 elif obj[7]<=182.14894461511594:
                                    return 'normal'
                                 else:
                                    return 'normal'
                              else:
                                 return 'normal'
                           else:
                              return 'normal'
                        elif obj[8]<=115.65300500900987:
                           # {"feature": "count", "instances": 11833, "metric_value": 0.6481, "depth": 9}
                           if obj[4]<=84.1075547934875:
                              # {"feature": "service", "instances": 11574, "metric_value": 0.6285, "depth": 10}
                              if obj[1]<=31.22646916402721:
                                 # {"feature": "dst_host_same_srv_rate", "instances": 7581, "metric_value": 0.5275, "depth": 11}
                                 if obj[9]<=0.5212416946488446:
                                    # {"feature": "dst_host_count", "instances": 5690, "metric_value": 0.3503, "depth": 12}
                                    if obj[7]<=182.14894461511594:
                                       # {"feature": "dst_host_diff_srv_rate", "instances": 3312, "metric_value": 0.1507, "depth": 13}
                                       if obj[10]<=0.6497142587290661:
                                          # {"feature": "diff_srv_rate", "instances": 3282, "metric_value": 0.1436, "depth": 14}
                                          if obj[6]<=0.0:
                                             # {"feature": "serror_rate", "instances": 3134, "metric_value": 0.1214, "depth": 15}
                                             if obj[5]<=0.7309383846979811:
                                                return 'normal'
                                             elif obj[5]>0.7309383846979811:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          elif obj[6]>0.0:
                                             # {"feature": "serror_rate", "instances": 148, "metric_value": 0.4145, "depth": 15}
                                             if obj[5]<=0.7309383846979811:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          else:
                                             return 'normal'
                                       elif obj[10]>0.6497142587290661:
                                          # {"feature": "diff_srv_rate", "instances": 30, "metric_value": 0.6275, "depth": 14}
                                          if obj[6]<=0.0:
                                             # {"feature": "serror_rate", "instances": 29, "metric_value": 0.6438, "depth": 15}
                                             if obj[5]<=0.7309383846979811:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          elif obj[6]>0.0:
                                             return 'normal'
                                          else:
                                             return 'normal'
                                       else:
                                          return 'normal'
                                    elif obj[7]>182.14894461511594:
                                       # {"feature": "diff_srv_rate", "instances": 2378, "metric_value": 0.5462, "depth": 13}
                                       if obj[6]<=0.0:
                                          # {"feature": "dst_host_diff_srv_rate", "instances": 2163, "metric_value": 0.5452, "depth": 14}
                                          if obj[10]<=0.6497142587290661:
                                             # {"feature": "serror_rate", "instances": 2145, "metric_value": 0.5482, "depth": 15}
                                             if obj[5]<=0.7309383846979811:
                                                return 'normal'
                                             elif obj[5]>0.7309383846979811:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          elif obj[10]>0.6497142587290661:
                                             return 'normal'
                                          else:
                                             return 'normal'
                                       elif obj[6]>0.0:
                                          # {"feature": "dst_host_diff_srv_rate", "instances": 215, "metric_value": 0.3874, "depth": 14}
                                          if obj[10]<=0.6497142587290661:
                                             # {"feature": "serror_rate", "instances": 210, "metric_value": 0.3945, "depth": 15}
                                             if obj[5]<=0.7309383846979811:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          elif obj[10]>0.6497142587290661:
                                             return 'normal'
                                          else:
                                             return 'normal'
                                       else:
                                          return 'normal'
                                    else:
                                       return 'normal'
                                 elif obj[9]>0.5212416946488446:
                                    # {"feature": "dst_host_diff_srv_rate", "instances": 1891, "metric_value": 0.6721, "depth": 12}
                                    if obj[10]<=0.6497142587290661:
                                       # {"feature": "dst_host_count", "instances": 1881, "metric_value": 0.6678, "depth": 13}
                                       if obj[7]<=182.14894461511594:
                                          # {"feature": "serror_rate", "instances": 1877, "metric_value": 0.6687, "depth": 14}
                                          if obj[5]<=0.7309383846979811:
                                             # {"feature": "diff_srv_rate", "instances": 1875, "metric_value": 0.6691, "depth": 15}
                                             if obj[6]<=0.0:
                                                return 'normal'
                                             elif obj[6]>0.0:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          elif obj[5]>0.7309383846979811:
                                             return 'normal'
                                          else:
                                             return 'normal'
                                       elif obj[7]>182.14894461511594:
                                          return 'normal'
                                       else:
                                          return 'normal'
                                    elif obj[10]>0.6497142587290661:
                                       # {"feature": "diff_srv_rate", "instances": 10, "metric_value": 0.469, "depth": 13}
                                       if obj[6]<=0.0:
                                          return 'normal'
                                       elif obj[6]>0.0:
                                          # {"feature": "serror_rate", "instances": 2, "metric_value": 1.0, "depth": 14}
                                          if obj[5]<=0.7309383846979811:
                                             # {"feature": "dst_host_count", "instances": 2, "metric_value": 1.0, "depth": 15}
                                             if obj[7]<=182.14894461511594:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          else:
                                             return 'normal'
                                       else:
                                          return 'normal'
                                    else:
                                       return 'normal'
                                 else:
                                    return 'normal'
                              elif obj[1]>31.22646916402721:
                                 # {"feature": "dst_host_same_srv_rate", "instances": 3993, "metric_value": 0.7225, "depth": 11}
                                 if obj[9]<=0.5212416946488446:
                                    # {"feature": "dst_host_diff_srv_rate", "instances": 2719, "metric_value": 0.8957, "depth": 12}
                                    if obj[10]<=0.6497142587290661:
                                       # {"feature": "dst_host_count", "instances": 2670, "metric_value": 0.8994, "depth": 13}
                                       if obj[7]>182.14894461511594:
                                          # {"feature": "diff_srv_rate", "instances": 1504, "metric_value": 0.9527, "depth": 14}
                                          if obj[6]<=0.0:
                                             # {"feature": "serror_rate", "instances": 1180, "metric_value": 1.0161, "depth": 15}
                                             if obj[5]<=0.7309383846979811:
                                                return 'normal'
                                             elif obj[5]>0.7309383846979811:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          elif obj[6]>0.0:
                                             # {"feature": "serror_rate", "instances": 324, "metric_value": 0.5267, "depth": 15}
                                             if obj[5]<=0.7309383846979811:
                                                return 'normal'
                                             elif obj[5]>0.7309383846979811:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          else:
                                             return 'normal'
                                       elif obj[7]<=182.14894461511594:
                                          # {"feature": "diff_srv_rate", "instances": 1166, "metric_value": 0.7113, "depth": 14}
                                          if obj[6]<=0.0:
                                             # {"feature": "serror_rate", "instances": 943, "metric_value": 0.7729, "depth": 15}
                                             if obj[5]<=0.7309383846979811:
                                                return 'normal'
                                             elif obj[5]>0.7309383846979811:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          elif obj[6]>0.0:
                                             # {"feature": "serror_rate", "instances": 223, "metric_value": 0.3384, "depth": 15}
                                             if obj[5]<=0.7309383846979811:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          else:
                                             return 'normal'
                                       else:
                                          return 'normal'
                                    elif obj[10]>0.6497142587290661:
                                       # {"feature": "dst_host_count", "instances": 49, "metric_value": 0.246, "depth": 13}
                                       if obj[7]>182.14894461511594:
                                          return 'normal'
                                       elif obj[7]<=182.14894461511594:
                                          # {"feature": "diff_srv_rate", "instances": 15, "metric_value": 0.5665, "depth": 14}
                                          if obj[6]<=0.0:
                                             # {"feature": "serror_rate", "instances": 13, "metric_value": 0.6194, "depth": 15}
                                             if obj[5]<=0.7309383846979811:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          elif obj[6]>0.0:
                                             return 'normal'
                                          else:
                                             return 'normal'
                                       else:
                                          return 'normal'
                                    else:
                                       return 'normal'
                                 elif obj[9]>0.5212416946488446:
                                    # {"feature": "serror_rate", "instances": 1274, "metric_value": 0.1191, "depth": 12}
                                    if obj[5]<=0.7309383846979811:
                                       # {"feature": "diff_srv_rate", "instances": 1266, "metric_value": 0.1145, "depth": 13}
                                       if obj[6]<=0.0:
                                          # {"feature": "dst_host_count", "instances": 1205, "metric_value": 0.1193, "depth": 14}
                                          if obj[7]<=182.14894461511594:
                                             # {"feature": "dst_host_diff_srv_rate", "instances": 1185, "metric_value": 0.1209, "depth": 15}
                                             if obj[10]<=0.6497142587290661:
                                                return 'normal'
                                             elif obj[10]>0.6497142587290661:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          elif obj[7]>182.14894461511594:
                                             return 'normal'
                                          else:
                                             return 'normal'
                                       elif obj[6]>0.0:
                                          return 'normal'
                                       else:
                                          return 'normal'
                                    elif obj[5]>0.7309383846979811:
                                       # {"feature": "diff_srv_rate", "instances": 8, "metric_value": 0.5436, "depth": 13}
                                       if obj[6]<=0.0:
                                          return 'normal'
                                       elif obj[6]>0.0:
                                          return 'u2r'
                                       else:
                                          return 'u2r'
                                    else:
                                       return 'normal'
                                 else:
                                    return 'normal'
                              else:
                                 return 'normal'
                           elif obj[4]>84.1075547934875:
                              # {"feature": "service", "instances": 259, "metric_value": 1.0431, "depth": 10}
                              if obj[1]<=31.22646916402721:
                                 return 'normal'
                              elif obj[1]>31.22646916402721:
                                 # {"feature": "serror_rate", "instances": 99, "metric_value": 0.6873, "depth": 11}
                                 if obj[5]<=0.7309383846979811:
                                    # {"feature": "diff_srv_rate", "instances": 93, "metric_value": 0.4503, "depth": 12}
                                    if obj[6]<=0.0:
                                       # {"feature": "dst_host_count", "instances": 71, "metric_value": 0.2133, "depth": 13}
                                       if obj[7]>182.14894461511594:
                                          # {"feature": "dst_host_same_srv_rate", "instances": 56, "metric_value": 0.258, "depth": 14}
                                          if obj[9]<=0.5212416946488446:
                                             # {"feature": "dst_host_diff_srv_rate", "instances": 56, "metric_value": 0.258, "depth": 15}
                                             if obj[10]<=0.6497142587290661:
                                                return 'dos'
                                             else:
                                                return 'dos'
                                          else:
                                             return 'dos'
                                       elif obj[7]<=182.14894461511594:
                                          return 'dos'
                                       else:
                                          return 'dos'
                                    elif obj[6]>0.0:
                                       # {"feature": "dst_host_count", "instances": 22, "metric_value": 0.9373, "depth": 13}
                                       if obj[7]>182.14894461511594:
                                          # {"feature": "dst_host_same_srv_rate", "instances": 21, "metric_value": 0.7025, "depth": 14}
                                          if obj[9]<=0.5212416946488446:
                                             # {"feature": "dst_host_diff_srv_rate", "instances": 21, "metric_value": 0.7025, "depth": 15}
                                             if obj[10]<=0.6497142587290661:
                                                return 'dos'
                                             else:
                                                return 'dos'
                                          else:
                                             return 'dos'
                                       elif obj[7]<=182.14894461511594:
                                          return 'normal'
                                       else:
                                          return 'normal'
                                    else:
                                       return 'dos'
                                 elif obj[5]>0.7309383846979811:
                                    return 'normal'
                                 else:
                                    return 'normal'
                              else:
                                 return 'dos'
                           else:
                              return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=6.97999571336715:
                        # {"feature": "dst_host_same_srv_rate", "instances": 455, "metric_value": 0.8648, "depth": 8}
                        if obj[9]>0.5212416946488446:
                           # {"feature": "serror_rate", "instances": 269, "metric_value": 0.9471, "depth": 9}
                           if obj[5]<=0.7309383846979811:
                              # {"feature": "service", "instances": 173, "metric_value": 1.0802, "depth": 10}
                              if obj[1]<=31.22646916402721:
                                 # {"feature": "dst_host_count", "instances": 169, "metric_value": 1.0381, "depth": 11}
                                 if obj[7]>182.14894461511594:
                                    # {"feature": "count", "instances": 91, "metric_value": 0.945, "depth": 12}
                                    if obj[4]<=84.1075547934875:
                                       # {"feature": "diff_srv_rate", "instances": 91, "metric_value": 0.945, "depth": 13}
                                       if obj[6]<=0.0:
                                          # {"feature": "dst_host_srv_count", "instances": 91, "metric_value": 0.945, "depth": 14}
                                          if obj[8]>115.65300500900987:
                                             # {"feature": "dst_host_diff_srv_rate", "instances": 91, "metric_value": 0.945, "depth": 15}
                                             if obj[10]<=0.6497142587290661:
                                                return 'dos'
                                             else:
                                                return 'dos'
                                          else:
                                             return 'dos'
                                       else:
                                          return 'dos'
                                    else:
                                       return 'dos'
                                 elif obj[7]<=182.14894461511594:
                                    # {"feature": "diff_srv_rate", "instances": 78, "metric_value": 0.5869, "depth": 12}
                                    if obj[6]<=0.0:
                                       # {"feature": "dst_host_srv_count", "instances": 77, "metric_value": 0.5571, "depth": 13}
                                       if obj[8]>115.65300500900987:
                                          # {"feature": "count", "instances": 68, "metric_value": 0.379, "depth": 14}
                                          if obj[4]<=84.1075547934875:
                                             # {"feature": "dst_host_diff_srv_rate", "instances": 68, "metric_value": 0.379, "depth": 15}
                                             if obj[10]<=0.6497142587290661:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          else:
                                             return 'normal'
                                       elif obj[8]<=115.65300500900987:
                                          # {"feature": "count", "instances": 9, "metric_value": 0.9911, "depth": 14}
                                          if obj[4]<=84.1075547934875:
                                             # {"feature": "dst_host_diff_srv_rate", "instances": 9, "metric_value": 0.9911, "depth": 15}
                                             if obj[10]<=0.6497142587290661:
                                                return 'dos'
                                             else:
                                                return 'dos'
                                          else:
                                             return 'dos'
                                       else:
                                          return 'dos'
                                    elif obj[6]>0.0:
                                       return 'dos'
                                    else:
                                       return 'dos'
                                 else:
                                    return 'normal'
                              elif obj[1]>31.22646916402721:
                                 # {"feature": "diff_srv_rate", "instances": 4, "metric_value": 0.8113, "depth": 11}
                                 if obj[6]<=0.0:
                                    # {"feature": "count", "instances": 2, "metric_value": 1.0, "depth": 12}
                                    if obj[4]<=84.1075547934875:
                                       # {"feature": "dst_host_count", "instances": 2, "metric_value": 1.0, "depth": 13}
                                       if obj[7]<=182.14894461511594:
                                          # {"feature": "dst_host_srv_count", "instances": 2, "metric_value": 1.0, "depth": 14}
                                          if obj[8]>115.65300500900987:
                                             # {"feature": "dst_host_diff_srv_rate", "instances": 2, "metric_value": 1.0, "depth": 15}
                                             if obj[10]<=0.6497142587290661:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          else:
                                             return 'normal'
                                       else:
                                          return 'normal'
                                    else:
                                       return 'normal'
                                 elif obj[6]>0.0:
                                    return 'normal'
                                 else:
                                    return 'normal'
                              else:
                                 return 'normal'
                           elif obj[5]>0.7309383846979811:
                              # {"feature": "dst_host_srv_count", "instances": 96, "metric_value": 0.0835, "depth": 10}
                              if obj[8]>115.65300500900987:
                                 return 'normal'
                              elif obj[8]<=115.65300500900987:
                                 # {"feature": "service", "instances": 7, "metric_value": 0.5917, "depth": 11}
                                 if obj[1]<=31.22646916402721:
                                    # {"feature": "count", "instances": 6, "metric_value": 0.65, "depth": 12}
                                    if obj[4]<=84.1075547934875:
                                       # {"feature": "diff_srv_rate", "instances": 6, "metric_value": 0.65, "depth": 13}
                                       if obj[6]<=0.0:
                                          # {"feature": "dst_host_count", "instances": 6, "metric_value": 0.65, "depth": 14}
                                          if obj[7]<=182.14894461511594:
                                             # {"feature": "dst_host_diff_srv_rate", "instances": 6, "metric_value": 0.65, "depth": 15}
                                             if obj[10]<=0.6497142587290661:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          else:
                                             return 'normal'
                                       else:
                                          return 'normal'
                                    else:
                                       return 'normal'
                                 elif obj[1]>31.22646916402721:
                                    return 'normal'
                                 else:
                                    return 'normal'
                              else:
                                 return 'normal'
                           else:
                              return 'normal'
                        elif obj[9]<=0.5212416946488446:
                           # {"feature": "serror_rate", "instances": 186, "metric_value": 0.3451, "depth": 9}
                           if obj[5]<=0.7309383846979811:
                              # {"feature": "diff_srv_rate", "instances": 121, "metric_value": 0.4395, "depth": 10}
                              if obj[6]<=0.0:
                                 # {"feature": "dst_host_count", "instances": 89, "metric_value": 0.5396, "depth": 11}
                                 if obj[7]<=182.14894461511594:
                                    # {"feature": "service", "instances": 67, "metric_value": 0.6442, "depth": 12}
                                    if obj[1]<=31.22646916402721:
                                       # {"feature": "count", "instances": 38, "metric_value": 0.3985, "depth": 13}
                                       if obj[4]<=84.1075547934875:
                                          # {"feature": "dst_host_srv_count", "instances": 38, "metric_value": 0.3985, "depth": 14}
                                          if obj[8]<=115.65300500900987:
                                             # {"feature": "dst_host_diff_srv_rate", "instances": 38, "metric_value": 0.3985, "depth": 15}
                                             if obj[10]<=0.6497142587290661:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          else:
                                             return 'normal'
                                       else:
                                          return 'normal'
                                    elif obj[1]>31.22646916402721:
                                       # {"feature": "count", "instances": 29, "metric_value": 0.8498, "depth": 13}
                                       if obj[4]<=84.1075547934875:
                                          # {"feature": "dst_host_srv_count", "instances": 29, "metric_value": 0.8498, "depth": 14}
                                          if obj[8]<=115.65300500900987:
                                             # {"feature": "dst_host_diff_srv_rate", "instances": 29, "metric_value": 0.8498, "depth": 15}
                                             if obj[10]<=0.6497142587290661:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          else:
                                             return 'normal'
                                       else:
                                          return 'normal'
                                    else:
                                       return 'normal'
                                 elif obj[7]>182.14894461511594:
                                    return 'normal'
                                 else:
                                    return 'normal'
                              elif obj[6]>0.0:
                                 return 'normal'
                              else:
                                 return 'normal'
                           elif obj[5]>0.7309383846979811:
                              # {"feature": "diff_srv_rate", "instances": 65, "metric_value": 0.1147, "depth": 10}
                              if obj[6]<=0.0:
                                 return 'normal'
                              elif obj[6]>0.0:
                                 return 'probe'
                              else:
                                 return 'probe'
                           else:
                              return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[3]<=0:
                     # {"feature": "count", "instances": 943, "metric_value": 1.1211, "depth": 7}
                     if obj[4]<=84.1075547934875:
                        # {"feature": "diff_srv_rate", "instances": 897, "metric_value": 0.9544, "depth": 8}
                        if obj[6]<=0.0:
                           # {"feature": "dst_host_diff_srv_rate", "instances": 730, "metric_value": 0.687, "depth": 9}
                           if obj[10]<=0.6497142587290661:
                              # {"feature": "serror_rate", "instances": 718, "metric_value": 0.643, "depth": 10}
                              if obj[5]<=0.7309383846979811:
                                 # {"feature": "dst_host_same_srv_rate", "instances": 670, "metric_value": 0.5276, "depth": 11}
                                 if obj[9]>0.5212416946488446:
                                    return 'normal'
                                 elif obj[9]<=0.5212416946488446:
                                    # {"feature": "flag", "instances": 237, "metric_value": 0.9225, "depth": 12}
                                    if obj[2]<=6.97999571336715:
                                       # {"feature": "dst_host_srv_count", "instances": 210, "metric_value": 0.9587, "depth": 13}
                                       if obj[8]<=115.65300500900987:
                                          # {"feature": "service", "instances": 188, "metric_value": 0.9839, "depth": 14}
                                          if obj[1]>31.22646916402721:
                                             # {"feature": "dst_host_count", "instances": 119, "metric_value": 0.9885, "depth": 15}
                                             if obj[7]<=182.14894461511594:
                                                return 'probe'
                                             elif obj[7]>182.14894461511594:
                                                return 'probe'
                                             else:
                                                return 'probe'
                                          elif obj[1]<=31.22646916402721:
                                             # {"feature": "dst_host_count", "instances": 69, "metric_value": 0.6981, "depth": 15}
                                             if obj[7]<=182.14894461511594:
                                                return 'normal'
                                             elif obj[7]>182.14894461511594:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          else:
                                             return 'normal'
                                       elif obj[8]>115.65300500900987:
                                          return 'normal'
                                       else:
                                          return 'normal'
                                    elif obj[2]>6.97999571336715:
                                       return 'normal'
                                    else:
                                       return 'normal'
                                 else:
                                    return 'normal'
                              elif obj[5]>0.7309383846979811:
                                 # {"feature": "flag", "instances": 48, "metric_value": 1.0104, "depth": 11}
                                 if obj[2]<=6.97999571336715:
                                    # {"feature": "dst_host_srv_count", "instances": 39, "metric_value": 0.8582, "depth": 12}
                                    if obj[8]<=115.65300500900987:
                                       # {"feature": "dst_host_same_srv_rate", "instances": 29, "metric_value": 0.9576, "depth": 13}
                                       if obj[9]<=0.5212416946488446:
                                          # {"feature": "service", "instances": 21, "metric_value": 0.5917, "depth": 14}
                                          if obj[1]>31.22646916402721:
                                             return 'normal'
                                          elif obj[1]<=31.22646916402721:
                                             # {"feature": "dst_host_count", "instances": 5, "metric_value": 0.971, "depth": 15}
                                             if obj[7]<=182.14894461511594:
                                                return 'dos'
                                             elif obj[7]>182.14894461511594:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          else:
                                             return 'dos'
                                       elif obj[9]>0.5212416946488446:
                                          return 'dos'
                                       else:
                                          return 'dos'
                                    elif obj[8]>115.65300500900987:
                                       return 'normal'
                                    else:
                                       return 'normal'
                                 elif obj[2]>6.97999571336715:
                                    # {"feature": "service", "instances": 9, "metric_value": 0.7642, "depth": 12}
                                    if obj[1]>31.22646916402721:
                                       return 'normal'
                                    elif obj[1]<=31.22646916402721:
                                       # {"feature": "dst_host_same_srv_rate", "instances": 4, "metric_value": 1.0, "depth": 13}
                                       if obj[9]<=0.5212416946488446:
                                          return 'normal'
                                       elif obj[9]>0.5212416946488446:
                                          return 'r2l'
                                       else:
                                          return 'r2l'
                                    else:
                                       return 'normal'
                                 else:
                                    return 'normal'
                              else:
                                 return 'normal'
                           elif obj[10]>0.6497142587290661:
                              # {"feature": "service", "instances": 12, "metric_value": 0.4138, "depth": 10}
                              if obj[1]>31.22646916402721:
                                 return 'probe'
                              elif obj[1]<=31.22646916402721:
                                 return 'dos'
                              else:
                                 return 'dos'
                           else:
                              return 'probe'
                        elif obj[6]>0.0:
                           # {"feature": "service", "instances": 167, "metric_value": 0.6138, "depth": 9}
                           if obj[1]>31.22646916402721:
                              # {"feature": "dst_host_srv_count", "instances": 128, "metric_value": 0.3373, "depth": 10}
                              if obj[8]<=115.65300500900987:
                                 # {"feature": "serror_rate", "instances": 126, "metric_value": 0.2762, "depth": 11}
                                 if obj[5]<=0.7309383846979811:
                                    # {"feature": "dst_host_diff_srv_rate", "instances": 95, "metric_value": 0.3399, "depth": 12}
                                    if obj[10]<=0.6497142587290661:
                                       # {"feature": "dst_host_count", "instances": 94, "metric_value": 0.2998, "depth": 13}
                                       if obj[7]>182.14894461511594:
                                          # {"feature": "flag", "instances": 78, "metric_value": 0.2352, "depth": 14}
                                          if obj[2]<=6.97999571336715:
                                             # {"feature": "dst_host_same_srv_rate", "instances": 78, "metric_value": 0.2352, "depth": 15}
                                             if obj[9]<=0.5212416946488446:
                                                return 'probe'
                                             else:
                                                return 'probe'
                                          else:
                                             return 'probe'
                                       elif obj[7]<=182.14894461511594:
                                          # {"feature": "flag", "instances": 16, "metric_value": 0.5436, "depth": 14}
                                          if obj[2]<=6.97999571336715:
                                             # {"feature": "dst_host_same_srv_rate", "instances": 14, "metric_value": 0.5917, "depth": 15}
                                             if obj[9]<=0.5212416946488446:
                                                return 'probe'
                                             else:
                                                return 'probe'
                                          elif obj[2]>6.97999571336715:
                                             return 'probe'
                                          else:
                                             return 'probe'
                                       else:
                                          return 'probe'
                                    elif obj[10]>0.6497142587290661:
                                       return 'normal'
                                    else:
                                       return 'normal'
                                 elif obj[5]>0.7309383846979811:
                                    return 'probe'
                                 else:
                                    return 'probe'
                              elif obj[8]>115.65300500900987:
                                 return 'normal'
                              else:
                                 return 'normal'
                           elif obj[1]<=31.22646916402721:
                              # {"feature": "flag", "instances": 39, "metric_value": 1.0971, "depth": 10}
                              if obj[2]<=6.97999571336715:
                                 # {"feature": "serror_rate", "instances": 35, "metric_value": 1.0362, "depth": 11}
                                 if obj[5]<=0.7309383846979811:
                                    # {"feature": "dst_host_same_srv_rate", "instances": 24, "metric_value": 1.1964, "depth": 12}
                                    if obj[9]<=0.5212416946488446:
                                       # {"feature": "dst_host_count", "instances": 23, "metric_value": 1.1916, "depth": 13}
                                       if obj[7]<=182.14894461511594:
                                          # {"feature": "dst_host_srv_count", "instances": 13, "metric_value": 1.3143, "depth": 14}
                                          if obj[8]<=115.65300500900987:
                                             # {"feature": "dst_host_diff_srv_rate", "instances": 13, "metric_value": 1.3143, "depth": 15}
                                             if obj[10]<=0.6497142587290661:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          else:
                                             return 'normal'
                                       elif obj[7]>182.14894461511594:
                                          # {"feature": "dst_host_srv_count", "instances": 10, "metric_value": 0.8813, "depth": 14}
                                          if obj[8]<=115.65300500900987:
                                             # {"feature": "dst_host_diff_srv_rate", "instances": 10, "metric_value": 0.8813, "depth": 15}
                                             if obj[10]<=0.6497142587290661:
                                                return 'probe'
                                             else:
                                                return 'probe'
                                          else:
                                             return 'probe'
                                       else:
                                          return 'probe'
                                    elif obj[9]>0.5212416946488446:
                                       return 'normal'
                                    else:
                                       return 'normal'
                                 elif obj[5]>0.7309383846979811:
                                    return 'probe'
                                 else:
                                    return 'probe'
                              elif obj[2]>6.97999571336715:
                                 return 'normal'
                              else:
                                 return 'normal'
                           else:
                              return 'probe'
                        else:
                           return 'probe'
                     elif obj[4]>84.1075547934875:
                        # {"feature": "dst_host_count", "instances": 46, "metric_value": 0.7131, "depth": 8}
                        if obj[7]<=182.14894461511594:
                           return 'dos'
                        elif obj[7]>182.14894461511594:
                           return 'probe'
                        else:
                           return 'probe'
                     else:
                        return 'dos'
                  else:
                     return 'normal'
               elif obj[11]>0.7663706668194779:
                  # {"feature": "service", "instances": 4985, "metric_value": 1.1482, "depth": 6}
                  if obj[1]>31.22646916402721:
                     # {"feature": "serror_rate", "instances": 2989, "metric_value": 0.8948, "depth": 7}
                     if obj[5]<=0.7309383846979811:
                        # {"feature": "dst_host_diff_srv_rate", "instances": 2988, "metric_value": 0.892, "depth": 8}
                        if obj[10]<=0.6497142587290661:
                           # {"feature": "diff_srv_rate", "instances": 2159, "metric_value": 1.0153, "depth": 9}
                           if obj[6]<=0.0:
                              # {"feature": "count", "instances": 1262, "metric_value": 0.8522, "depth": 10}
                              if obj[4]<=84.1075547934875:
                                 # {"feature": "dst_host_same_srv_rate", "instances": 903, "metric_value": 1.0098, "depth": 11}
                                 if obj[9]<=0.5212416946488446:
                                    # {"feature": "dst_host_count", "instances": 582, "metric_value": 0.4744, "depth": 12}
                                    if obj[7]>182.14894461511594:
                                       # {"feature": "flag", "instances": 559, "metric_value": 0.4406, "depth": 13}
                                       if obj[2]>6.97999571336715:
                                          # {"feature": "src_bytes", "instances": 559, "metric_value": 0.4406, "depth": 14}
                                          if obj[3]>0:
                                             # {"feature": "dst_host_srv_count", "instances": 559, "metric_value": 0.4406, "depth": 15}
                                             if obj[8]<=115.65300500900987:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          else:
                                             return 'normal'
                                       else:
                                          return 'normal'
                                    elif obj[7]<=182.14894461511594:
                                       # {"feature": "flag", "instances": 23, "metric_value": 0.5586, "depth": 13}
                                       if obj[2]>6.97999571336715:
                                          # {"feature": "src_bytes", "instances": 23, "metric_value": 0.5586, "depth": 14}
                                          if obj[3]>0:
                                             # {"feature": "dst_host_srv_count", "instances": 23, "metric_value": 0.5586, "depth": 15}
                                             if obj[8]<=115.65300500900987:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          else:
                                             return 'normal'
                                       else:
                                          return 'normal'
                                    else:
                                       return 'normal'
                                 elif obj[9]>0.5212416946488446:
                                    # {"feature": "src_bytes", "instances": 321, "metric_value": 1.0572, "depth": 12}
                                    if obj[3]>0:
                                       # {"feature": "dst_host_count", "instances": 319, "metric_value": 1.0517, "depth": 13}
                                       if obj[7]<=182.14894461511594:
                                          # {"feature": "dst_host_srv_count", "instances": 232, "metric_value": 1.1839, "depth": 14}
                                          if obj[8]<=115.65300500900987:
                                             # {"feature": "flag", "instances": 182, "metric_value": 1.2333, "depth": 15}
                                             if obj[2]>6.97999571336715:
                                                return 'probe'
                                             else:
                                                return 'probe'
                                          elif obj[8]>115.65300500900987:
                                             # {"feature": "flag", "instances": 50, "metric_value": 0.9248, "depth": 15}
                                             if obj[2]>6.97999571336715:
                                                return 'probe'
                                             else:
                                                return 'probe'
                                          else:
                                             return 'probe'
                                       elif obj[7]>182.14894461511594:
                                          # {"feature": "flag", "instances": 87, "metric_value": 0.4798, "depth": 14}
                                          if obj[2]>6.97999571336715:
                                             # {"feature": "dst_host_srv_count", "instances": 87, "metric_value": 0.4798, "depth": 15}
                                             if obj[8]>115.65300500900987:
                                                return 'probe'
                                             else:
                                                return 'probe'
                                          else:
                                             return 'probe'
                                       else:
                                          return 'probe'
                                    elif obj[3]<=0:
                                       return 'normal'
                                    else:
                                       return 'normal'
                                 else:
                                    return 'probe'
                              elif obj[4]>84.1075547934875:
                                 return 'normal'
                              else:
                                 return 'normal'
                           elif obj[6]>0.0:
                              # {"feature": "count", "instances": 897, "metric_value": 0.9684, "depth": 10}
                              if obj[4]<=84.1075547934875:
                                 # {"feature": "dst_host_count", "instances": 730, "metric_value": 0.9995, "depth": 11}
                                 if obj[7]>182.14894461511594:
                                    # {"feature": "dst_host_same_srv_rate", "instances": 697, "metric_value": 0.9958, "depth": 12}
                                    if obj[9]<=0.5212416946488446:
                                       # {"feature": "dst_host_srv_count", "instances": 696, "metric_value": 0.9957, "depth": 13}
                                       if obj[8]<=115.65300500900987:
                                          # {"feature": "flag", "instances": 693, "metric_value": 0.9961, "depth": 14}
                                          if obj[2]>6.97999571336715:
                                             # {"feature": "src_bytes", "instances": 693, "metric_value": 0.9961, "depth": 15}
                                             if obj[3]>0:
                                                return 'probe'
                                             else:
                                                return 'probe'
                                          else:
                                             return 'probe'
                                       elif obj[8]>115.65300500900987:
                                          return 'probe'
                                       else:
                                          return 'probe'
                                    elif obj[9]>0.5212416946488446:
                                       return 'normal'
                                    else:
                                       return 'normal'
                                 elif obj[7]<=182.14894461511594:
                                    return 'normal'
                                 else:
                                    return 'normal'
                              elif obj[4]>84.1075547934875:
                                 return 'probe'
                              else:
                                 return 'probe'
                           else:
                              return 'probe'
                        elif obj[10]>0.6497142587290661:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]>0.7309383846979811:
                        return 'r2l'
                     else:
                        return 'r2l'
                  elif obj[1]<=31.22646916402721:
                     # {"feature": "dst_host_srv_count", "instances": 1996, "metric_value": 0.8938, "depth": 7}
                     if obj[8]<=115.65300500900987:
                        # {"feature": "src_bytes", "instances": 1196, "metric_value": 1.0764, "depth": 8}
                        if obj[3]>0:
                           # {"feature": "diff_srv_rate", "instances": 1158, "metric_value": 1.0213, "depth": 9}
                           if obj[6]<=0.0:
                              # {"feature": "flag", "instances": 1136, "metric_value": 1.0245, "depth": 10}
                              if obj[2]>6.97999571336715:
                                 # {"feature": "count", "instances": 1135, "metric_value": 1.0246, "depth": 11}
                                 if obj[4]<=84.1075547934875:
                                    # {"feature": "serror_rate", "instances": 1135, "metric_value": 1.0246, "depth": 12}
                                    if obj[5]<=0.7309383846979811:
                                       # {"feature": "dst_host_count", "instances": 1135, "metric_value": 1.0246, "depth": 13}
                                       if obj[7]<=182.14894461511594:
                                          # {"feature": "dst_host_same_srv_rate", "instances": 1135, "metric_value": 1.0246, "depth": 14}
                                          if obj[9]>0.5212416946488446:
                                             # {"feature": "dst_host_diff_srv_rate", "instances": 1135, "metric_value": 1.0246, "depth": 15}
                                             if obj[10]<=0.6497142587290661:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          else:
                                             return 'normal'
                                       else:
                                          return 'normal'
                                    else:
                                       return 'normal'
                                 else:
                                    return 'normal'
                              elif obj[2]<=6.97999571336715:
                                 return 'normal'
                              else:
                                 return 'normal'
                           elif obj[6]>0.0:
                              # {"feature": "flag", "instances": 22, "metric_value": 0.2668, "depth": 10}
                              if obj[2]>6.97999571336715:
                                 # {"feature": "count", "instances": 22, "metric_value": 0.2668, "depth": 11}
                                 if obj[4]<=84.1075547934875:
                                    # {"feature": "serror_rate", "instances": 22, "metric_value": 0.2668, "depth": 12}
                                    if obj[5]<=0.7309383846979811:
                                       # {"feature": "dst_host_count", "instances": 22, "metric_value": 0.2668, "depth": 13}
                                       if obj[7]<=182.14894461511594:
                                          # {"feature": "dst_host_same_srv_rate", "instances": 22, "metric_value": 0.2668, "depth": 14}
                                          if obj[9]>0.5212416946488446:
                                             # {"feature": "dst_host_diff_srv_rate", "instances": 22, "metric_value": 0.2668, "depth": 15}
                                             if obj[10]<=0.6497142587290661:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          else:
                                             return 'normal'
                                       else:
                                          return 'normal'
                                    else:
                                       return 'normal'
                                 else:
                                    return 'normal'
                              else:
                                 return 'normal'
                           else:
                              return 'normal'
                        elif obj[3]<=0:
                           # {"feature": "flag", "instances": 38, "metric_value": 1.2315, "depth": 9}
                           if obj[2]>6.97999571336715:
                              # {"feature": "count", "instances": 38, "metric_value": 1.2315, "depth": 10}
                              if obj[4]<=84.1075547934875:
                                 # {"feature": "serror_rate", "instances": 38, "metric_value": 1.2315, "depth": 11}
                                 if obj[5]<=0.7309383846979811:
                                    # {"feature": "diff_srv_rate", "instances": 38, "metric_value": 1.2315, "depth": 12}
                                    if obj[6]<=0.0:
                                       # {"feature": "dst_host_count", "instances": 38, "metric_value": 1.2315, "depth": 13}
                                       if obj[7]<=182.14894461511594:
                                          # {"feature": "dst_host_same_srv_rate", "instances": 38, "metric_value": 1.2315, "depth": 14}
                                          if obj[9]>0.5212416946488446:
                                             # {"feature": "dst_host_diff_srv_rate", "instances": 38, "metric_value": 1.2315, "depth": 15}
                                             if obj[10]<=0.6497142587290661:
                                                return 'r2l'
                                             else:
                                                return 'r2l'
                                          else:
                                             return 'r2l'
                                       else:
                                          return 'r2l'
                                    else:
                                       return 'r2l'
                                 else:
                                    return 'r2l'
                              else:
                                 return 'r2l'
                           else:
                              return 'r2l'
                        else:
                           return 'r2l'
                     elif obj[8]>115.65300500900987:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            elif obj[0]<=0:
               # {"feature": "count", "instances": 5160, "metric_value": 1.4984, "depth": 5}
               if obj[4]<=84.1075547934875:
                  # {"feature": "dst_host_count", "instances": 2964, "metric_value": 1.4305, "depth": 6}
                  if obj[7]<=182.14894461511594:
                     # {"feature": "service", "instances": 1698, "metric_value": 0.9304, "depth": 7}
                     if obj[1]<=31.22646916402721:
                        # {"feature": "dst_host_diff_srv_rate", "instances": 1640, "metric_value": 0.8695, "depth": 8}
                        if obj[10]<=0.6497142587290661:
                           # {"feature": "dst_host_same_src_port_rate", "instances": 1623, "metric_value": 0.8453, "depth": 9}
                           if obj[11]>0.7663706668194779:
                              # {"feature": "dst_host_same_srv_rate", "instances": 1535, "metric_value": 0.7285, "depth": 10}
                              if obj[9]>0.5212416946488446:
                                 # {"feature": "diff_srv_rate", "instances": 1533, "metric_value": 0.7274, "depth": 11}
                                 if obj[6]<=0.0:
                                    # {"feature": "dst_host_srv_count", "instances": 1526, "metric_value": 0.7296, "depth": 12}
                                    if obj[8]>115.65300500900987:
                                       # {"feature": "flag", "instances": 771, "metric_value": 0.8624, "depth": 13}
                                       if obj[2]>6.97999571336715:
                                          # {"feature": "src_bytes", "instances": 771, "metric_value": 0.8624, "depth": 14}
                                          if obj[3]>0:
                                             # {"feature": "serror_rate", "instances": 771, "metric_value": 0.8624, "depth": 15}
                                             if obj[5]<=0.7309383846979811:
                                                return 'probe'
                                             else:
                                                return 'probe'
                                          else:
                                             return 'probe'
                                       else:
                                          return 'probe'
                                    elif obj[8]<=115.65300500900987:
                                       # {"feature": "flag", "instances": 755, "metric_value": 0.5522, "depth": 13}
                                       if obj[2]>6.97999571336715:
                                          # {"feature": "src_bytes", "instances": 755, "metric_value": 0.5522, "depth": 14}
                                          if obj[3]>0:
                                             # {"feature": "serror_rate", "instances": 755, "metric_value": 0.5522, "depth": 15}
                                             if obj[5]<=0.7309383846979811:
                                                return 'probe'
                                             else:
                                                return 'probe'
                                          else:
                                             return 'probe'
                                       else:
                                          return 'probe'
                                    else:
                                       return 'probe'
                                 elif obj[6]>0.0:
                                    return 'probe'
                                 else:
                                    return 'probe'
                              elif obj[9]<=0.5212416946488446:
                                 # {"feature": "flag", "instances": 2, "metric_value": 1.0, "depth": 11}
                                 if obj[2]>6.97999571336715:
                                    # {"feature": "src_bytes", "instances": 2, "metric_value": 1.0, "depth": 12}
                                    if obj[3]>0:
                                       # {"feature": "serror_rate", "instances": 2, "metric_value": 1.0, "depth": 13}
                                       if obj[5]<=0.7309383846979811:
                                          # {"feature": "diff_srv_rate", "instances": 2, "metric_value": 1.0, "depth": 14}
                                          if obj[6]<=0.0:
                                             # {"feature": "dst_host_srv_count", "instances": 2, "metric_value": 1.0, "depth": 15}
                                             if obj[8]<=115.65300500900987:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          else:
                                             return 'normal'
                                       else:
                                          return 'normal'
                                    else:
                                       return 'normal'
                                 else:
                                    return 'normal'
                              else:
                                 return 'normal'
                           elif obj[11]<=0.7663706668194779:
                              # {"feature": "dst_host_srv_count", "instances": 88, "metric_value": 1.502, "depth": 10}
                              if obj[8]<=115.65300500900987:
                                 # {"feature": "dst_host_same_srv_rate", "instances": 79, "metric_value": 1.4409, "depth": 11}
                                 if obj[9]<=0.5212416946488446:
                                    # {"feature": "diff_srv_rate", "instances": 76, "metric_value": 1.3981, "depth": 12}
                                    if obj[6]<=0.0:
                                       # {"feature": "flag", "instances": 73, "metric_value": 1.4208, "depth": 13}
                                       if obj[2]>6.97999571336715:
                                          # {"feature": "src_bytes", "instances": 73, "metric_value": 1.4208, "depth": 14}
                                          if obj[3]>0:
                                             # {"feature": "serror_rate", "instances": 73, "metric_value": 1.4208, "depth": 15}
                                             if obj[5]<=0.7309383846979811:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          else:
                                             return 'normal'
                                       else:
                                          return 'normal'
                                    elif obj[6]>0.0:
                                       return 'normal'
                                    else:
                                       return 'normal'
                                 elif obj[9]>0.5212416946488446:
                                    return 'probe'
                                 else:
                                    return 'probe'
                              elif obj[8]>115.65300500900987:
                                 # {"feature": "dst_host_same_srv_rate", "instances": 9, "metric_value": 0.9911, "depth": 11}
                                 if obj[9]>0.5212416946488446:
                                    # {"feature": "flag", "instances": 6, "metric_value": 0.65, "depth": 12}
                                    if obj[2]>6.97999571336715:
                                       # {"feature": "src_bytes", "instances": 6, "metric_value": 0.65, "depth": 13}
                                       if obj[3]>0:
                                          # {"feature": "serror_rate", "instances": 6, "metric_value": 0.65, "depth": 14}
                                          if obj[5]<=0.7309383846979811:
                                             # {"feature": "diff_srv_rate", "instances": 6, "metric_value": 0.65, "depth": 15}
                                             if obj[6]<=0.0:
                                                return 'dos'
                                             else:
                                                return 'dos'
                                          else:
                                             return 'dos'
                                       else:
                                          return 'dos'
                                    else:
                                       return 'dos'
                                 elif obj[9]<=0.5212416946488446:
                                    return 'probe'
                                 else:
                                    return 'probe'
                              else:
                                 return 'dos'
                           else:
                              return 'normal'
                        elif obj[10]>0.6497142587290661:
                           # {"feature": "diff_srv_rate", "instances": 17, "metric_value": 0.874, "depth": 9}
                           if obj[6]<=0.0:
                              # {"feature": "dst_host_srv_count", "instances": 16, "metric_value": 0.8113, "depth": 10}
                              if obj[8]>115.65300500900987:
                                 # {"feature": "flag", "instances": 12, "metric_value": 0.65, "depth": 11}
                                 if obj[2]>6.97999571336715:
                                    # {"feature": "src_bytes", "instances": 12, "metric_value": 0.65, "depth": 12}
                                    if obj[3]>0:
                                       # {"feature": "serror_rate", "instances": 12, "metric_value": 0.65, "depth": 13}
                                       if obj[5]<=0.7309383846979811:
                                          # {"feature": "dst_host_same_srv_rate", "instances": 12, "metric_value": 0.65, "depth": 14}
                                          if obj[9]<=0.5212416946488446:
                                             # {"feature": "dst_host_same_src_port_rate", "instances": 6, "metric_value": 0.65, "depth": 15}
                                             if obj[11]<=0.7663706668194779:
                                                return 'dos'
                                             else:
                                                return 'dos'
                                          elif obj[9]>0.5212416946488446:
                                             # {"feature": "dst_host_same_src_port_rate", "instances": 6, "metric_value": 0.65, "depth": 15}
                                             if obj[11]<=0.7663706668194779:
                                                return 'dos'
                                             else:
                                                return 'dos'
                                          else:
                                             return 'dos'
                                       else:
                                          return 'dos'
                                    else:
                                       return 'dos'
                                 else:
                                    return 'dos'
                              elif obj[8]<=115.65300500900987:
                                 # {"feature": "dst_host_same_srv_rate", "instances": 4, "metric_value": 1.0, "depth": 11}
                                 if obj[9]<=0.5212416946488446:
                                    # {"feature": "flag", "instances": 3, "metric_value": 0.9183, "depth": 12}
                                    if obj[2]>6.97999571336715:
                                       # {"feature": "src_bytes", "instances": 3, "metric_value": 0.9183, "depth": 13}
                                       if obj[3]>0:
                                          # {"feature": "serror_rate", "instances": 3, "metric_value": 0.9183, "depth": 14}
                                          if obj[5]<=0.7309383846979811:
                                             # {"feature": "dst_host_same_src_port_rate", "instances": 3, "metric_value": 0.9183, "depth": 15}
                                             if obj[11]<=0.7663706668194779:
                                                return 'probe'
                                             else:
                                                return 'probe'
                                          else:
                                             return 'probe'
                                       else:
                                          return 'probe'
                                    else:
                                       return 'probe'
                                 elif obj[9]>0.5212416946488446:
                                    return 'dos'
                                 else:
                                    return 'dos'
                              else:
                                 return 'probe'
                           elif obj[6]>0.0:
                              return 'probe'
                           else:
                              return 'probe'
                        else:
                           return 'dos'
                     elif obj[1]>31.22646916402721:
                        # {"feature": "dst_host_same_srv_rate", "instances": 58, "metric_value": 0.5833, "depth": 8}
                        if obj[9]<=0.5212416946488446:
                           # {"feature": "dst_host_diff_srv_rate", "instances": 53, "metric_value": 0.3138, "depth": 9}
                           if obj[10]<=0.6497142587290661:
                              # {"feature": "diff_srv_rate", "instances": 51, "metric_value": 0.2387, "depth": 10}
                              if obj[6]<=0.0:
                                 # {"feature": "flag", "instances": 29, "metric_value": 0.3621, "depth": 11}
                                 if obj[2]>6.97999571336715:
                                    # {"feature": "src_bytes", "instances": 29, "metric_value": 0.3621, "depth": 12}
                                    if obj[3]>0:
                                       # {"feature": "serror_rate", "instances": 29, "metric_value": 0.3621, "depth": 13}
                                       if obj[5]<=0.7309383846979811:
                                          # {"feature": "dst_host_srv_count", "instances": 29, "metric_value": 0.3621, "depth": 14}
                                          if obj[8]<=115.65300500900987:
                                             # {"feature": "dst_host_same_src_port_rate", "instances": 29, "metric_value": 0.3621, "depth": 15}
                                             if obj[11]<=0.7663706668194779:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          else:
                                             return 'normal'
                                       else:
                                          return 'normal'
                                    else:
                                       return 'normal'
                                 else:
                                    return 'normal'
                              elif obj[6]>0.0:
                                 return 'normal'
                              else:
                                 return 'normal'
                           elif obj[10]>0.6497142587290661:
                              # {"feature": "diff_srv_rate", "instances": 2, "metric_value": 1.0, "depth": 10}
                              if obj[6]<=0.0:
                                 return 'probe'
                              elif obj[6]>0.0:
                                 return 'normal'
                              else:
                                 return 'normal'
                           else:
                              return 'normal'
                        elif obj[9]>0.5212416946488446:
                           # {"feature": "flag", "instances": 5, "metric_value": 0.971, "depth": 9}
                           if obj[2]>6.97999571336715:
                              # {"feature": "src_bytes", "instances": 5, "metric_value": 0.971, "depth": 10}
                              if obj[3]>0:
                                 # {"feature": "serror_rate", "instances": 5, "metric_value": 0.971, "depth": 11}
                                 if obj[5]<=0.7309383846979811:
                                    # {"feature": "diff_srv_rate", "instances": 5, "metric_value": 0.971, "depth": 12}
                                    if obj[6]<=0.0:
                                       # {"feature": "dst_host_srv_count", "instances": 5, "metric_value": 0.971, "depth": 13}
                                       if obj[8]<=115.65300500900987:
                                          # {"feature": "dst_host_diff_srv_rate", "instances": 5, "metric_value": 0.971, "depth": 14}
                                          if obj[10]<=0.6497142587290661:
                                             # {"feature": "dst_host_same_src_port_rate", "instances": 5, "metric_value": 0.971, "depth": 15}
                                             if obj[11]>0.7663706668194779:
                                                return 'dos'
                                             else:
                                                return 'dos'
                                          else:
                                             return 'dos'
                                       else:
                                          return 'dos'
                                    else:
                                       return 'dos'
                                 else:
                                    return 'dos'
                              else:
                                 return 'dos'
                           else:
                              return 'dos'
                        else:
                           return 'dos'
                     else:
                        return 'normal'
                  elif obj[7]>182.14894461511594:
                     # {"feature": "diff_srv_rate", "instances": 1266, "metric_value": 0.8438, "depth": 7}
                     if obj[6]>0.0:
                        return 'normal'
                     elif obj[6]<=0.0:
                        # {"feature": "service", "instances": 557, "metric_value": 1.0763, "depth": 8}
                        if obj[1]<=31.22646916402721:
                           # {"feature": "dst_host_same_src_port_rate", "instances": 512, "metric_value": 1.0596, "depth": 9}
                           if obj[11]>0.7663706668194779:
                              # {"feature": "flag", "instances": 313, "metric_value": 0.9998, "depth": 10}
                              if obj[2]>6.97999571336715:
                                 # {"feature": "src_bytes", "instances": 313, "metric_value": 0.9998, "depth": 11}
                                 if obj[3]>0:
                                    # {"feature": "serror_rate", "instances": 313, "metric_value": 0.9998, "depth": 12}
                                    if obj[5]<=0.7309383846979811:
                                       # {"feature": "dst_host_srv_count", "instances": 313, "metric_value": 0.9998, "depth": 13}
                                       if obj[8]>115.65300500900987:
                                          # {"feature": "dst_host_same_srv_rate", "instances": 313, "metric_value": 0.9998, "depth": 14}
                                          if obj[9]>0.5212416946488446:
                                             # {"feature": "dst_host_diff_srv_rate", "instances": 313, "metric_value": 0.9998, "depth": 15}
                                             if obj[10]<=0.6497142587290661:
                                                return 'dos'
                                             else:
                                                return 'dos'
                                          else:
                                             return 'dos'
                                       else:
                                          return 'dos'
                                    else:
                                       return 'dos'
                                 else:
                                    return 'dos'
                              else:
                                 return 'dos'
                           elif obj[11]<=0.7663706668194779:
                              # {"feature": "dst_host_srv_count", "instances": 199, "metric_value": 0.9861, "depth": 10}
                              if obj[8]<=115.65300500900987:
                                 # {"feature": "flag", "instances": 197, "metric_value": 0.9916, "depth": 11}
                                 if obj[2]>6.97999571336715:
                                    # {"feature": "src_bytes", "instances": 197, "metric_value": 0.9916, "depth": 12}
                                    if obj[3]>0:
                                       # {"feature": "serror_rate", "instances": 197, "metric_value": 0.9916, "depth": 13}
                                       if obj[5]<=0.7309383846979811:
                                          # {"feature": "dst_host_same_srv_rate", "instances": 197, "metric_value": 0.9916, "depth": 14}
                                          if obj[9]<=0.5212416946488446:
                                             # {"feature": "dst_host_diff_srv_rate", "instances": 197, "metric_value": 0.9916, "depth": 15}
                                             if obj[10]<=0.6497142587290661:
                                                return 'dos'
                                             else:
                                                return 'dos'
                                          else:
                                             return 'dos'
                                       else:
                                          return 'dos'
                                    else:
                                       return 'dos'
                                 else:
                                    return 'dos'
                              elif obj[8]>115.65300500900987:
                                 return 'dos'
                              else:
                                 return 'dos'
                           else:
                              return 'dos'
                        elif obj[1]>31.22646916402721:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'dos'
                  else:
                     return 'normal'
               elif obj[4]>84.1075547934875:
                  # {"feature": "serror_rate", "instances": 2196, "metric_value": 0.0114, "depth": 6}
                  if obj[5]<=0.7309383846979811:
                     return 'dos'
                  elif obj[5]>0.7309383846979811:
                     # {"feature": "dst_host_count", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[7]<=182.14894461511594:
                        return 'probe'
                     elif obj[7]>182.14894461511594:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'dos'
            else:
               return 'dos'
         elif obj[14]>0.11883181316631937:
            # {"feature": "dst_host_same_srv_rate", "instances": 17272, "metric_value": 1.5643, "depth": 4}
            if obj[9]<=0.5212416946488446:
               # {"feature": "dst_host_diff_srv_rate", "instances": 13658, "metric_value": 1.2154, "depth": 5}
               if obj[10]<=0.6497142587290661:
                  # {"feature": "count", "instances": 9989, "metric_value": 1.057, "depth": 6}
                  if obj[4]>84.1075547934875:
                     # {"feature": "dst_host_same_src_port_rate", "instances": 7137, "metric_value": 0.3488, "depth": 7}
                     if obj[11]<=0.7663706668194779:
                        # {"feature": "serror_rate", "instances": 6915, "metric_value": 0.219, "depth": 8}
                        if obj[5]<=0.7309383846979811:
                           # {"feature": "src_bytes", "instances": 6911, "metric_value": 0.2163, "depth": 9}
                           if obj[3]<=0:
                              # {"feature": "service", "instances": 6770, "metric_value": 0.2053, "depth": 10}
                              if obj[1]>31.22646916402721:
                                 # {"feature": "dst_host_count", "instances": 4267, "metric_value": 0.2678, "depth": 11}
                                 if obj[7]>182.14894461511594:
                                    # {"feature": "protocol_type", "instances": 4108, "metric_value": 0.2755, "depth": 12}
                                    if obj[0]>0:
                                       # {"feature": "flag", "instances": 4108, "metric_value": 0.2755, "depth": 13}
                                       if obj[2]<=6.97999571336715:
                                          # {"feature": "diff_srv_rate", "instances": 4108, "metric_value": 0.2755, "depth": 14}
                                          if obj[6]>0.0:
                                             # {"feature": "dst_host_srv_count", "instances": 4108, "metric_value": 0.2755, "depth": 15}
                                             if obj[8]<=115.65300500900987:
                                                return 'dos'
                                             else:
                                                return 'dos'
                                          else:
                                             return 'dos'
                                       else:
                                          return 'dos'
                                    else:
                                       return 'dos'
                                 elif obj[7]<=182.14894461511594:
                                    return 'dos'
                                 else:
                                    return 'dos'
                              elif obj[1]<=31.22646916402721:
                                 # {"feature": "protocol_type", "instances": 2503, "metric_value": 0.0754, "depth": 11}
                                 if obj[0]>0:
                                    # {"feature": "flag", "instances": 2503, "metric_value": 0.0754, "depth": 12}
                                    if obj[2]<=6.97999571336715:
                                       # {"feature": "diff_srv_rate", "instances": 2503, "metric_value": 0.0754, "depth": 13}
                                       if obj[6]>0.0:
                                          # {"feature": "dst_host_count", "instances": 2503, "metric_value": 0.0754, "depth": 14}
                                          if obj[7]>182.14894461511594:
                                             # {"feature": "dst_host_srv_count", "instances": 2503, "metric_value": 0.0754, "depth": 15}
                                             if obj[8]<=115.65300500900987:
                                                return 'dos'
                                             else:
                                                return 'dos'
                                          else:
                                             return 'dos'
                                       else:
                                          return 'dos'
                                    else:
                                       return 'dos'
                                 else:
                                    return 'dos'
                              else:
                                 return 'dos'
                           elif obj[3]>0:
                              # {"feature": "flag", "instances": 141, "metric_value": 0.5324, "depth": 10}
                              if obj[2]>6.97999571336715:
                                 # {"feature": "diff_srv_rate", "instances": 139, "metric_value": 0.4778, "depth": 11}
                                 if obj[6]<=0.0:
                                    # {"feature": "protocol_type", "instances": 105, "metric_value": 0.1361, "depth": 12}
                                    if obj[0]<=0:
                                       return 'dos'
                                    elif obj[0]>0:
                                       # {"feature": "service", "instances": 17, "metric_value": 0.5226, "depth": 13}
                                       if obj[1]>31.22646916402721:
                                          # {"feature": "dst_host_count", "instances": 17, "metric_value": 0.5226, "depth": 14}
                                          if obj[7]>182.14894461511594:
                                             # {"feature": "dst_host_srv_count", "instances": 17, "metric_value": 0.5226, "depth": 15}
                                             if obj[8]<=115.65300500900987:
                                                return 'dos'
                                             else:
                                                return 'dos'
                                          else:
                                             return 'dos'
                                       else:
                                          return 'dos'
                                    else:
                                       return 'dos'
                                 elif obj[6]>0.0:
                                    # {"feature": "service", "instances": 34, "metric_value": 1.0768, "depth": 12}
                                    if obj[1]>31.22646916402721:
                                       # {"feature": "protocol_type", "instances": 33, "metric_value": 1.0304, "depth": 13}
                                       if obj[0]>0:
                                          # {"feature": "dst_host_count", "instances": 33, "metric_value": 1.0304, "depth": 14}
                                          if obj[7]>182.14894461511594:
                                             # {"feature": "dst_host_srv_count", "instances": 33, "metric_value": 1.0304, "depth": 15}
                                             if obj[8]<=115.65300500900987:
                                                return 'dos'
                                             else:
                                                return 'dos'
                                          else:
                                             return 'dos'
                                       else:
                                          return 'dos'
                                    elif obj[1]<=31.22646916402721:
                                       return 'probe'
                                    else:
                                       return 'probe'
                                 else:
                                    return 'dos'
                              elif obj[2]<=6.97999571336715:
                                 return 'probe'
                              else:
                                 return 'probe'
                           else:
                              return 'dos'
                        elif obj[5]>0.7309383846979811:
                           return 'probe'
                        else:
                           return 'probe'
                     elif obj[11]>0.7663706668194779:
                        return 'probe'
                     else:
                        return 'probe'
                  elif obj[4]<=84.1075547934875:
                     # {"feature": "serror_rate", "instances": 2852, "metric_value": 1.2975, "depth": 7}
                     if obj[5]<=0.7309383846979811:
                        # {"feature": "service", "instances": 2830, "metric_value": 1.2883, "depth": 8}
                        if obj[1]>31.22646916402721:
                           # {"feature": "protocol_type", "instances": 2403, "metric_value": 1.1065, "depth": 9}
                           if obj[0]>0:
                              # {"feature": "flag", "instances": 2402, "metric_value": 1.1055, "depth": 10}
                              if obj[2]<=6.97999571336715:
                                 # {"feature": "diff_srv_rate", "instances": 1581, "metric_value": 0.7405, "depth": 11}
                                 if obj[6]<=0.0:
                                    # {"feature": "dst_host_count", "instances": 904, "metric_value": 0.1607, "depth": 12}
                                    if obj[7]>182.14894461511594:
                                       # {"feature": "src_bytes", "instances": 721, "metric_value": 0.1206, "depth": 13}
                                       if obj[3]<=0:
                                          # {"feature": "dst_host_same_src_port_rate", "instances": 422, "metric_value": 0.1857, "depth": 14}
                                          if obj[11]<=0.7663706668194779:
                                             # {"feature": "dst_host_srv_count", "instances": 364, "metric_value": 0.2088, "depth": 15}
                                             if obj[8]<=115.65300500900987:
                                                return 'probe'
                                             else:
                                                return 'probe'
                                          elif obj[11]>0.7663706668194779:
                                             return 'probe'
                                          else:
                                             return 'probe'
                                       elif obj[3]>0:
                                          return 'probe'
                                       else:
                                          return 'probe'
                                    elif obj[7]<=182.14894461511594:
                                       # {"feature": "src_bytes", "instances": 183, "metric_value": 0.2342, "depth": 13}
                                       if obj[3]<=0:
                                          # {"feature": "dst_host_srv_count", "instances": 157, "metric_value": 0.0556, "depth": 14}
                                          if obj[8]<=115.65300500900987:
                                             # {"feature": "dst_host_same_src_port_rate", "instances": 156, "metric_value": 0.0559, "depth": 15}
                                             if obj[11]<=0.7663706668194779:
                                                return 'probe'
                                             else:
                                                return 'probe'
                                          elif obj[8]>115.65300500900987:
                                             return 'probe'
                                          else:
                                             return 'probe'
                                       elif obj[3]>0:
                                          # {"feature": "dst_host_srv_count", "instances": 26, "metric_value": 0.7793, "depth": 14}
                                          if obj[8]<=115.65300500900987:
                                             # {"feature": "dst_host_same_src_port_rate", "instances": 26, "metric_value": 0.7793, "depth": 15}
                                             if obj[11]<=0.7663706668194779:
                                                return 'probe'
                                             else:
                                                return 'probe'
                                          else:
                                             return 'probe'
                                       else:
                                          return 'probe'
                                    else:
                                       return 'probe'
                                 elif obj[6]>0.0:
                                    # {"feature": "src_bytes", "instances": 677, "metric_value": 0.9954, "depth": 12}
                                    if obj[3]<=0:
                                       # {"feature": "dst_host_count", "instances": 672, "metric_value": 0.982, "depth": 13}
                                       if obj[7]>182.14894461511594:
                                          # {"feature": "dst_host_same_src_port_rate", "instances": 627, "metric_value": 0.9932, "depth": 14}
                                          if obj[11]<=0.7663706668194779:
                                             # {"feature": "dst_host_srv_count", "instances": 625, "metric_value": 0.9936, "depth": 15}
                                             if obj[8]<=115.65300500900987:
                                                return 'probe'
                                             else:
                                                return 'probe'
                                          elif obj[11]>0.7663706668194779:
                                             return 'probe'
                                          else:
                                             return 'probe'
                                       elif obj[7]<=182.14894461511594:
                                          return 'probe'
                                       else:
                                          return 'probe'
                                    elif obj[3]>0:
                                       # {"feature": "dst_host_same_src_port_rate", "instances": 5, "metric_value": 0.7219, "depth": 13}
                                       if obj[11]<=0.7663706668194779:
                                          # {"feature": "dst_host_count", "instances": 3, "metric_value": 0.9183, "depth": 14}
                                          if obj[7]>182.14894461511594:
                                             # {"feature": "dst_host_srv_count", "instances": 3, "metric_value": 0.9183, "depth": 15}
                                             if obj[8]<=115.65300500900987:
                                                return 'probe'
                                             else:
                                                return 'probe'
                                          else:
                                             return 'probe'
                                       elif obj[11]>0.7663706668194779:
                                          return 'probe'
                                       else:
                                          return 'probe'
                                    else:
                                       return 'probe'
                                 else:
                                    return 'probe'
                              elif obj[2]>6.97999571336715:
                                 # {"feature": "dst_host_count", "instances": 821, "metric_value": 1.4421, "depth": 11}
                                 if obj[7]>182.14894461511594:
                                    # {"feature": "diff_srv_rate", "instances": 740, "metric_value": 1.3614, "depth": 12}
                                    if obj[6]>0.0:
                                       # {"feature": "dst_host_same_src_port_rate", "instances": 433, "metric_value": 0.6156, "depth": 13}
                                       if obj[11]<=0.7663706668194779:
                                          # {"feature": "dst_host_srv_count", "instances": 367, "metric_value": 0.6817, "depth": 14}
                                          if obj[8]<=115.65300500900987:
                                             # {"feature": "src_bytes", "instances": 366, "metric_value": 0.6828, "depth": 15}
                                             if obj[3]>0:
                                                return 'probe'
                                             else:
                                                return 'probe'
                                          elif obj[8]>115.65300500900987:
                                             return 'probe'
                                          else:
                                             return 'probe'
                                       elif obj[11]>0.7663706668194779:
                                          return 'probe'
                                       else:
                                          return 'probe'
                                    elif obj[6]<=0.0:
                                       # {"feature": "dst_host_same_src_port_rate", "instances": 307, "metric_value": 1.6135, "depth": 13}
                                       if obj[11]<=0.7663706668194779:
                                          # {"feature": "dst_host_srv_count", "instances": 290, "metric_value": 1.5939, "depth": 14}
                                          if obj[8]<=115.65300500900987:
                                             # {"feature": "src_bytes", "instances": 271, "metric_value": 1.5847, "depth": 15}
                                             if obj[3]>0:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          elif obj[8]>115.65300500900987:
                                             # {"feature": "src_bytes", "instances": 19, "metric_value": 0.2975, "depth": 15}
                                             if obj[3]>0:
                                                return 'dos'
                                             else:
                                                return 'dos'
                                          else:
                                             return 'dos'
                                       elif obj[11]>0.7663706668194779:
                                          return 'probe'
                                       else:
                                          return 'probe'
                                    else:
                                       return 'normal'
                                 elif obj[7]<=182.14894461511594:
                                    # {"feature": "dst_host_srv_count", "instances": 81, "metric_value": 0.3343, "depth": 12}
                                    if obj[8]<=115.65300500900987:
                                       return 'normal'
                                    elif obj[8]>115.65300500900987:
                                       # {"feature": "src_bytes", "instances": 12, "metric_value": 0.9799, "depth": 13}
                                       if obj[3]>0:
                                          # {"feature": "diff_srv_rate", "instances": 12, "metric_value": 0.9799, "depth": 14}
                                          if obj[6]<=0.0:
                                             # {"feature": "dst_host_same_src_port_rate", "instances": 12, "metric_value": 0.9799, "depth": 15}
                                             if obj[11]<=0.7663706668194779:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          else:
                                             return 'normal'
                                       else:
                                          return 'normal'
                                    else:
                                       return 'normal'
                                 else:
                                    return 'normal'
                              else:
                                 return 'probe'
                           elif obj[0]<=0:
                              return 'normal'
                           else:
                              return 'normal'
                        elif obj[1]<=31.22646916402721:
                           # {"feature": "src_bytes", "instances": 427, "metric_value": 1.1859, "depth": 9}
                           if obj[3]>0:
                              # {"feature": "protocol_type", "instances": 301, "metric_value": 0.6675, "depth": 10}
                              if obj[0]>0:
                                 # {"feature": "dst_host_same_src_port_rate", "instances": 288, "metric_value": 0.4601, "depth": 11}
                                 if obj[11]<=0.7663706668194779:
                                    # {"feature": "diff_srv_rate", "instances": 281, "metric_value": 0.3833, "depth": 12}
                                    if obj[6]<=0.0:
                                       # {"feature": "flag", "instances": 255, "metric_value": 0.2565, "depth": 13}
                                       if obj[2]>6.97999571336715:
                                          # {"feature": "dst_host_count", "instances": 179, "metric_value": 0.1228, "depth": 14}
                                          if obj[7]>182.14894461511594:
                                             # {"feature": "dst_host_srv_count", "instances": 110, "metric_value": 0.1805, "depth": 15}
                                             if obj[8]<=115.65300500900987:
                                                return 'normal'
                                             elif obj[8]>115.65300500900987:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          elif obj[7]<=182.14894461511594:
                                             return 'normal'
                                          else:
                                             return 'normal'
                                       elif obj[2]<=6.97999571336715:
                                          # {"feature": "dst_host_count", "instances": 76, "metric_value": 0.4855, "depth": 14}
                                          if obj[7]<=182.14894461511594:
                                             # {"feature": "dst_host_srv_count", "instances": 72, "metric_value": 0.3095, "depth": 15}
                                             if obj[8]<=115.65300500900987:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          elif obj[7]>182.14894461511594:
                                             return 'probe'
                                          else:
                                             return 'probe'
                                       else:
                                          return 'normal'
                                    elif obj[6]>0.0:
                                       # {"feature": "dst_host_count", "instances": 26, "metric_value": 0.9612, "depth": 13}
                                       if obj[7]<=182.14894461511594:
                                          # {"feature": "flag", "instances": 20, "metric_value": 0.7219, "depth": 14}
                                          if obj[2]<=6.97999571336715:
                                             # {"feature": "dst_host_srv_count", "instances": 16, "metric_value": 0.3373, "depth": 15}
                                             if obj[8]<=115.65300500900987:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          elif obj[2]>6.97999571336715:
                                             # {"feature": "dst_host_srv_count", "instances": 4, "metric_value": 0.8113, "depth": 15}
                                             if obj[8]<=115.65300500900987:
                                                return 'probe'
                                             else:
                                                return 'probe'
                                          else:
                                             return 'probe'
                                       elif obj[7]>182.14894461511594:
                                          return 'probe'
                                       else:
                                          return 'probe'
                                    else:
                                       return 'normal'
                                 elif obj[11]>0.7663706668194779:
                                    return 'probe'
                                 else:
                                    return 'probe'
                              elif obj[0]<=0:
                                 # {"feature": "dst_host_count", "instances": 13, "metric_value": 1.1401, "depth": 11}
                                 if obj[7]<=182.14894461511594:
                                    # {"feature": "diff_srv_rate", "instances": 11, "metric_value": 0.8659, "depth": 12}
                                    if obj[6]<=0.0:
                                       # {"feature": "flag", "instances": 10, "metric_value": 0.469, "depth": 13}
                                       if obj[2]>6.97999571336715:
                                          # {"feature": "dst_host_srv_count", "instances": 10, "metric_value": 0.469, "depth": 14}
                                          if obj[8]<=115.65300500900987:
                                             # {"feature": "dst_host_same_src_port_rate", "instances": 10, "metric_value": 0.469, "depth": 15}
                                             if obj[11]<=0.7663706668194779:
                                                return 'dos'
                                             else:
                                                return 'dos'
                                          else:
                                             return 'dos'
                                       else:
                                          return 'dos'
                                    elif obj[6]>0.0:
                                       return 'probe'
                                    else:
                                       return 'probe'
                                 elif obj[7]>182.14894461511594:
                                    return 'probe'
                                 else:
                                    return 'probe'
                              else:
                                 return 'dos'
                           elif obj[3]<=0:
                              # {"feature": "diff_srv_rate", "instances": 126, "metric_value": 1.4134, "depth": 10}
                              if obj[6]<=0.0:
                                 # {"feature": "dst_host_count", "instances": 77, "metric_value": 0.9226, "depth": 11}
                                 if obj[7]<=182.14894461511594:
                                    # {"feature": "flag", "instances": 48, "metric_value": 0.995, "depth": 12}
                                    if obj[2]<=6.97999571336715:
                                       # {"feature": "dst_host_srv_count", "instances": 47, "metric_value": 0.9971, "depth": 13}
                                       if obj[8]<=115.65300500900987:
                                          # {"feature": "protocol_type", "instances": 46, "metric_value": 0.9986, "depth": 14}
                                          if obj[0]>0:
                                             # {"feature": "dst_host_same_src_port_rate", "instances": 46, "metric_value": 0.9986, "depth": 15}
                                             if obj[11]<=0.7663706668194779:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          else:
                                             return 'normal'
                                       elif obj[8]>115.65300500900987:
                                          return 'normal'
                                       else:
                                          return 'normal'
                                    elif obj[2]>6.97999571336715:
                                       return 'normal'
                                    else:
                                       return 'normal'
                                 elif obj[7]>182.14894461511594:
                                    return 'probe'
                                 else:
                                    return 'probe'
                              elif obj[6]>0.0:
                                 # {"feature": "dst_host_count", "instances": 49, "metric_value": 0.9852, "depth": 11}
                                 if obj[7]>182.14894461511594:
                                    # {"feature": "protocol_type", "instances": 47, "metric_value": 0.9734, "depth": 12}
                                    if obj[0]>0:
                                       # {"feature": "flag", "instances": 47, "metric_value": 0.9734, "depth": 13}
                                       if obj[2]<=6.97999571336715:
                                          # {"feature": "dst_host_srv_count", "instances": 47, "metric_value": 0.9734, "depth": 14}
                                          if obj[8]<=115.65300500900987:
                                             # {"feature": "dst_host_same_src_port_rate", "instances": 47, "metric_value": 0.9734, "depth": 15}
                                             if obj[11]<=0.7663706668194779:
                                                return 'dos'
                                             else:
                                                return 'dos'
                                          else:
                                             return 'dos'
                                       else:
                                          return 'dos'
                                    else:
                                       return 'dos'
                                 elif obj[7]<=182.14894461511594:
                                    return 'probe'
                                 else:
                                    return 'probe'
                              else:
                                 return 'dos'
                           else:
                              return 'probe'
                        else:
                           return 'normal'
                     elif obj[5]>0.7309383846979811:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'probe'
               elif obj[10]>0.6497142587290661:
                  # {"feature": "serror_rate", "instances": 3669, "metric_value": 0.399, "depth": 6}
                  if obj[5]<=0.7309383846979811:
                     # {"feature": "dst_host_count", "instances": 3622, "metric_value": 0.3533, "depth": 7}
                     if obj[7]>182.14894461511594:
                        # {"feature": "flag", "instances": 3317, "metric_value": 0.1798, "depth": 8}
                        if obj[2]<=6.97999571336715:
                           return 'probe'
                        elif obj[2]>6.97999571336715:
                           # {"feature": "count", "instances": 432, "metric_value": 0.7383, "depth": 9}
                           if obj[4]<=84.1075547934875:
                              # {"feature": "diff_srv_rate", "instances": 347, "metric_value": 0.5071, "depth": 10}
                              if obj[6]>0.0:
                                 return 'probe'
                              elif obj[6]<=0.0:
                                 # {"feature": "protocol_type", "instances": 77, "metric_value": 0.9999, "depth": 11}
                                 if obj[0]>0:
                                    # {"feature": "service", "instances": 73, "metric_value": 0.9966, "depth": 12}
                                    if obj[1]>31.22646916402721:
                                       # {"feature": "src_bytes", "instances": 73, "metric_value": 0.9966, "depth": 13}
                                       if obj[3]>0:
                                          # {"feature": "dst_host_srv_count", "instances": 73, "metric_value": 0.9966, "depth": 14}
                                          if obj[8]<=115.65300500900987:
                                             # {"feature": "dst_host_same_src_port_rate", "instances": 73, "metric_value": 0.9966, "depth": 15}
                                             if obj[11]<=0.7663706668194779:
                                                return 'dos'
                                             else:
                                                return 'dos'
                                          else:
                                             return 'dos'
                                       else:
                                          return 'dos'
                                    else:
                                       return 'dos'
                                 elif obj[0]<=0:
                                    return 'probe'
                                 else:
                                    return 'probe'
                              else:
                                 return 'dos'
                           elif obj[4]>84.1075547934875:
                              # {"feature": "service", "instances": 85, "metric_value": 0.971, "depth": 10}
                              if obj[1]>31.22646916402721:
                                 # {"feature": "protocol_type", "instances": 78, "metric_value": 0.9306, "depth": 11}
                                 if obj[0]>0:
                                    # {"feature": "src_bytes", "instances": 78, "metric_value": 0.9306, "depth": 12}
                                    if obj[3]>0:
                                       # {"feature": "diff_srv_rate", "instances": 78, "metric_value": 0.9306, "depth": 13}
                                       if obj[6]>0.0:
                                          # {"feature": "dst_host_srv_count", "instances": 78, "metric_value": 0.9306, "depth": 14}
                                          if obj[8]<=115.65300500900987:
                                             # {"feature": "dst_host_same_src_port_rate", "instances": 78, "metric_value": 0.9306, "depth": 15}
                                             if obj[11]<=0.7663706668194779:
                                                return 'dos'
                                             else:
                                                return 'dos'
                                          else:
                                             return 'dos'
                                       else:
                                          return 'dos'
                                    else:
                                       return 'dos'
                                 else:
                                    return 'dos'
                              elif obj[1]<=31.22646916402721:
                                 return 'probe'
                              else:
                                 return 'probe'
                           else:
                              return 'dos'
                        else:
                           return 'probe'
                     elif obj[7]<=182.14894461511594:
                        # {"feature": "src_bytes", "instances": 305, "metric_value": 0.9226, "depth": 8}
                        if obj[3]<=0:
                           # {"feature": "service", "instances": 206, "metric_value": 0.1382, "depth": 9}
                           if obj[1]>31.22646916402721:
                              # {"feature": "flag", "instances": 183, "metric_value": 0.0869, "depth": 10}
                              if obj[2]<=6.97999571336715:
                                 # {"feature": "protocol_type", "instances": 168, "metric_value": 0.0932, "depth": 11}
                                 if obj[0]>0:
                                    # {"feature": "count", "instances": 168, "metric_value": 0.0932, "depth": 12}
                                    if obj[4]<=84.1075547934875:
                                       # {"feature": "diff_srv_rate", "instances": 168, "metric_value": 0.0932, "depth": 13}
                                       if obj[6]<=0.0:
                                          # {"feature": "dst_host_srv_count", "instances": 168, "metric_value": 0.0932, "depth": 14}
                                          if obj[8]<=115.65300500900987:
                                             # {"feature": "dst_host_same_src_port_rate", "instances": 168, "metric_value": 0.0932, "depth": 15}
                                             if obj[11]<=0.7663706668194779:
                                                return 'probe'
                                             else:
                                                return 'probe'
                                          else:
                                             return 'probe'
                                       else:
                                          return 'probe'
                                    else:
                                       return 'probe'
                                 else:
                                    return 'probe'
                              elif obj[2]>6.97999571336715:
                                 return 'probe'
                              else:
                                 return 'probe'
                           elif obj[1]<=31.22646916402721:
                              # {"feature": "flag", "instances": 23, "metric_value": 0.4262, "depth": 10}
                              if obj[2]>6.97999571336715:
                                 return 'probe'
                              elif obj[2]<=6.97999571336715:
                                 # {"feature": "dst_host_srv_count", "instances": 11, "metric_value": 0.684, "depth": 11}
                                 if obj[8]<=115.65300500900987:
                                    # {"feature": "protocol_type", "instances": 10, "metric_value": 0.7219, "depth": 12}
                                    if obj[0]>0:
                                       # {"feature": "count", "instances": 10, "metric_value": 0.7219, "depth": 13}
                                       if obj[4]<=84.1075547934875:
                                          # {"feature": "diff_srv_rate", "instances": 10, "metric_value": 0.7219, "depth": 14}
                                          if obj[6]<=0.0:
                                             # {"feature": "dst_host_same_src_port_rate", "instances": 10, "metric_value": 0.7219, "depth": 15}
                                             if obj[11]<=0.7663706668194779:
                                                return 'probe'
                                             else:
                                                return 'probe'
                                          else:
                                             return 'probe'
                                       else:
                                          return 'probe'
                                    else:
                                       return 'probe'
                                 elif obj[8]>115.65300500900987:
                                    return 'probe'
                                 else:
                                    return 'probe'
                              else:
                                 return 'probe'
                           else:
                              return 'probe'
                        elif obj[3]>0:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'probe'
                  elif obj[5]>0.7309383846979811:
                     # {"feature": "flag", "instances": 47, "metric_value": 0.9253, "depth": 7}
                     if obj[2]>6.97999571336715:
                        return 'dos'
                     elif obj[2]<=6.97999571336715:
                        # {"feature": "src_bytes", "instances": 12, "metric_value": 0.4138, "depth": 8}
                        if obj[3]<=0:
                           return 'probe'
                        elif obj[3]>0:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'probe'
                  else:
                     return 'dos'
               else:
                  return 'probe'
            elif obj[9]>0.5212416946488446:
               # {"feature": "protocol_type", "instances": 3614, "metric_value": 0.5534, "depth": 5}
               if obj[0]>0:
                  # {"feature": "service", "instances": 3508, "metric_value": 0.4499, "depth": 6}
                  if obj[1]<=31.22646916402721:
                     # {"feature": "dst_host_srv_count", "instances": 3338, "metric_value": 0.2641, "depth": 7}
                     if obj[8]>115.65300500900987:
                        # {"feature": "dst_host_count", "instances": 2700, "metric_value": 0.0088, "depth": 8}
                        if obj[7]<=182.14894461511594:
                           # {"feature": "src_bytes", "instances": 2560, "metric_value": 0.005, "depth": 9}
                           if obj[3]<=0:
                              # {"feature": "dst_host_same_src_port_rate", "instances": 2027, "metric_value": 0.0061, "depth": 10}
                              if obj[11]<=0.7663706668194779:
                                 # {"feature": "serror_rate", "instances": 1833, "metric_value": 0.0067, "depth": 11}
                                 if obj[5]<=0.7309383846979811:
                                    # {"feature": "flag", "instances": 1821, "metric_value": 0.0067, "depth": 12}
                                    if obj[2]<=6.97999571336715:
                                       # {"feature": "count", "instances": 1821, "metric_value": 0.0067, "depth": 13}
                                       if obj[4]<=84.1075547934875:
                                          # {"feature": "diff_srv_rate", "instances": 1821, "metric_value": 0.0067, "depth": 14}
                                          if obj[6]<=0.0:
                                             # {"feature": "dst_host_diff_srv_rate", "instances": 1821, "metric_value": 0.0067, "depth": 15}
                                             if obj[10]<=0.6497142587290661:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          else:
                                             return 'normal'
                                       else:
                                          return 'normal'
                                    else:
                                       return 'normal'
                                 elif obj[5]>0.7309383846979811:
                                    return 'normal'
                                 else:
                                    return 'normal'
                              elif obj[11]>0.7663706668194779:
                                 return 'normal'
                              else:
                                 return 'normal'
                           elif obj[3]>0:
                              return 'normal'
                           else:
                              return 'normal'
                        elif obj[7]>182.14894461511594:
                           # {"feature": "flag", "instances": 140, "metric_value": 0.0612, "depth": 9}
                           if obj[2]<=6.97999571336715:
                              # {"feature": "count", "instances": 88, "metric_value": 0.0897, "depth": 10}
                              if obj[4]<=84.1075547934875:
                                 # {"feature": "src_bytes", "instances": 81, "metric_value": 0.096, "depth": 11}
                                 if obj[3]<=0:
                                    # {"feature": "serror_rate", "instances": 81, "metric_value": 0.096, "depth": 12}
                                    if obj[5]<=0.7309383846979811:
                                       # {"feature": "diff_srv_rate", "instances": 81, "metric_value": 0.096, "depth": 13}
                                       if obj[6]<=0.0:
                                          # {"feature": "dst_host_diff_srv_rate", "instances": 81, "metric_value": 0.096, "depth": 14}
                                          if obj[10]<=0.6497142587290661:
                                             # {"feature": "dst_host_same_src_port_rate", "instances": 81, "metric_value": 0.096, "depth": 15}
                                             if obj[11]<=0.7663706668194779:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          else:
                                             return 'normal'
                                       else:
                                          return 'normal'
                                    else:
                                       return 'normal'
                                 else:
                                    return 'normal'
                              elif obj[4]>84.1075547934875:
                                 return 'normal'
                              else:
                                 return 'normal'
                           elif obj[2]>6.97999571336715:
                              return 'normal'
                           else:
                              return 'normal'
                        else:
                           return 'normal'
                     elif obj[8]<=115.65300500900987:
                        # {"feature": "src_bytes", "instances": 638, "metric_value": 0.8564, "depth": 8}
                        if obj[3]<=0:
                           # {"feature": "dst_host_same_src_port_rate", "instances": 472, "metric_value": 0.1709, "depth": 9}
                           if obj[11]<=0.7663706668194779:
                              return 'normal'
                           elif obj[11]>0.7663706668194779:
                              # {"feature": "flag", "instances": 66, "metric_value": 0.684, "depth": 10}
                              if obj[2]<=6.97999571336715:
                                 # {"feature": "count", "instances": 66, "metric_value": 0.684, "depth": 11}
                                 if obj[4]<=84.1075547934875:
                                    # {"feature": "serror_rate", "instances": 66, "metric_value": 0.684, "depth": 12}
                                    if obj[5]<=0.7309383846979811:
                                       # {"feature": "diff_srv_rate", "instances": 66, "metric_value": 0.684, "depth": 13}
                                       if obj[6]<=0.0:
                                          # {"feature": "dst_host_count", "instances": 66, "metric_value": 0.684, "depth": 14}
                                          if obj[7]<=182.14894461511594:
                                             # {"feature": "dst_host_diff_srv_rate", "instances": 66, "metric_value": 0.684, "depth": 15}
                                             if obj[10]<=0.6497142587290661:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          else:
                                             return 'normal'
                                       else:
                                          return 'normal'
                                    else:
                                       return 'normal'
                                 else:
                                    return 'normal'
                              else:
                                 return 'normal'
                           else:
                              return 'normal'
                        elif obj[3]>0:
                           # {"feature": "dst_host_same_src_port_rate", "instances": 166, "metric_value": 1.0687, "depth": 9}
                           if obj[11]<=0.7663706668194779:
                              # {"feature": "serror_rate", "instances": 156, "metric_value": 0.8829, "depth": 10}
                              if obj[5]<=0.7309383846979811:
                                 # {"feature": "diff_srv_rate", "instances": 152, "metric_value": 0.8594, "depth": 11}
                                 if obj[6]<=0.0:
                                    # {"feature": "flag", "instances": 150, "metric_value": 0.8462, "depth": 12}
                                    if obj[2]>6.97999571336715:
                                       # {"feature": "count", "instances": 122, "metric_value": 0.7912, "depth": 13}
                                       if obj[4]<=84.1075547934875:
                                          # {"feature": "dst_host_count", "instances": 122, "metric_value": 0.7912, "depth": 14}
                                          if obj[7]<=182.14894461511594:
                                             # {"feature": "dst_host_diff_srv_rate", "instances": 122, "metric_value": 0.7912, "depth": 15}
                                             if obj[10]<=0.6497142587290661:
                                                return 'dos'
                                             else:
                                                return 'dos'
                                          else:
                                             return 'dos'
                                       else:
                                          return 'dos'
                                    elif obj[2]<=6.97999571336715:
                                       # {"feature": "count", "instances": 28, "metric_value": 0.9852, "depth": 13}
                                       if obj[4]<=84.1075547934875:
                                          # {"feature": "dst_host_count", "instances": 28, "metric_value": 0.9852, "depth": 14}
                                          if obj[7]<=182.14894461511594:
                                             # {"feature": "dst_host_diff_srv_rate", "instances": 28, "metric_value": 0.9852, "depth": 15}
                                             if obj[10]<=0.6497142587290661:
                                                return 'dos'
                                             else:
                                                return 'dos'
                                          else:
                                             return 'dos'
                                       else:
                                          return 'dos'
                                    else:
                                       return 'dos'
                                 elif obj[6]>0.0:
                                    return 'normal'
                                 else:
                                    return 'normal'
                              elif obj[5]>0.7309383846979811:
                                 return 'normal'
                              else:
                                 return 'normal'
                           elif obj[11]>0.7663706668194779:
                              # {"feature": "flag", "instances": 10, "metric_value": 1.361, "depth": 10}
                              if obj[2]<=6.97999571336715:
                                 # {"feature": "count", "instances": 6, "metric_value": 1.2516, "depth": 11}
                                 if obj[4]<=84.1075547934875:
                                    # {"feature": "serror_rate", "instances": 6, "metric_value": 1.2516, "depth": 12}
                                    if obj[5]<=0.7309383846979811:
                                       # {"feature": "diff_srv_rate", "instances": 6, "metric_value": 1.2516, "depth": 13}
                                       if obj[6]<=0.0:
                                          # {"feature": "dst_host_count", "instances": 6, "metric_value": 1.2516, "depth": 14}
                                          if obj[7]<=182.14894461511594:
                                             # {"feature": "dst_host_diff_srv_rate", "instances": 6, "metric_value": 1.2516, "depth": 15}
                                             if obj[10]<=0.6497142587290661:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          else:
                                             return 'normal'
                                       else:
                                          return 'normal'
                                    else:
                                       return 'normal'
                                 else:
                                    return 'normal'
                              elif obj[2]>6.97999571336715:
                                 return 'r2l'
                              else:
                                 return 'r2l'
                           else:
                              return 'r2l'
                        else:
                           return 'dos'
                     else:
                        return 'normal'
                  elif obj[1]>31.22646916402721:
                     # {"feature": "serror_rate", "instances": 170, "metric_value": 1.6753, "depth": 7}
                     if obj[5]<=0.7309383846979811:
                        # {"feature": "dst_host_count", "instances": 169, "metric_value": 1.6492, "depth": 8}
                        if obj[7]<=182.14894461511594:
                           # {"feature": "count", "instances": 118, "metric_value": 1.5107, "depth": 9}
                           if obj[4]<=84.1075547934875:
                              # {"feature": "src_bytes", "instances": 104, "metric_value": 1.1179, "depth": 10}
                              if obj[3]>0:
                                 # {"feature": "dst_host_diff_srv_rate", "instances": 56, "metric_value": 0.5208, "depth": 11}
                                 if obj[10]<=0.6497142587290661:
                                    # {"feature": "diff_srv_rate", "instances": 54, "metric_value": 0.3606, "depth": 12}
                                    if obj[6]<=0.0:
                                       # {"feature": "flag", "instances": 53, "metric_value": 0.2695, "depth": 13}
                                       if obj[2]<=6.97999571336715:
                                          return 'r2l'
                                       elif obj[2]>6.97999571336715:
                                          # {"feature": "dst_host_srv_count", "instances": 4, "metric_value": 1.5, "depth": 14}
                                          if obj[8]<=115.65300500900987:
                                             # {"feature": "dst_host_same_src_port_rate", "instances": 4, "metric_value": 1.5, "depth": 15}
                                             if obj[11]<=0.7663706668194779:
                                                return 'r2l'
                                             else:
                                                return 'r2l'
                                          else:
                                             return 'r2l'
                                       else:
                                          return 'r2l'
                                    elif obj[6]>0.0:
                                       return 'u2r'
                                    else:
                                       return 'u2r'
                                 elif obj[10]>0.6497142587290661:
                                    return 'normal'
                                 else:
                                    return 'normal'
                              elif obj[3]<=0:
                                 return 'normal'
                              else:
                                 return 'normal'
                           elif obj[4]>84.1075547934875:
                              return 'dos'
                           else:
                              return 'dos'
                        elif obj[7]>182.14894461511594:
                           return 'dos'
                        else:
                           return 'dos'
                     elif obj[5]>0.7309383846979811:
                        return 'u2r'
                     else:
                        return 'u2r'
                  else:
                     return 'dos'
               elif obj[0]<=0:
                  return 'dos'
               else:
                  return 'dos'
            else:
               return 'normal'
         else:
            return 'dos'
      elif obj[12]>0.37023252388068995:
         # {"feature": "protocol_type", "instances": 3662, "metric_value": 0.736, "depth": 3}
         if obj[0]<=0:
            # {"feature": "service", "instances": 2915, "metric_value": 0.2906, "depth": 4}
            if obj[1]<=31.22646916402721:
               # {"feature": "dst_host_diff_srv_rate", "instances": 2914, "metric_value": 0.2888, "depth": 5}
               if obj[10]<=0.6497142587290661:
                  # {"feature": "diff_srv_rate", "instances": 2900, "metric_value": 0.2682, "depth": 6}
                  if obj[6]<=0.0:
                     # {"feature": "dst_host_same_srv_rate", "instances": 2897, "metric_value": 0.2646, "depth": 7}
                     if obj[9]>0.5212416946488446:
                        # {"feature": "dst_host_srv_count", "instances": 2888, "metric_value": 0.2552, "depth": 8}
                        if obj[8]<=115.65300500900987:
                           # {"feature": "flag", "instances": 2052, "metric_value": 0.2707, "depth": 9}
                           if obj[2]>6.97999571336715:
                              # {"feature": "src_bytes", "instances": 2052, "metric_value": 0.2707, "depth": 10}
                              if obj[3]>0:
                                 # {"feature": "count", "instances": 2052, "metric_value": 0.2707, "depth": 11}
                                 if obj[4]<=84.1075547934875:
                                    # {"feature": "serror_rate", "instances": 2052, "metric_value": 0.2707, "depth": 12}
                                    if obj[5]<=0.7309383846979811:
                                       # {"feature": "dst_host_count", "instances": 2052, "metric_value": 0.2707, "depth": 13}
                                       if obj[7]<=182.14894461511594:
                                          # {"feature": "dst_host_same_src_port_rate", "instances": 2052, "metric_value": 0.2707, "depth": 14}
                                          if obj[11]>0.7663706668194779:
                                             # {"feature": "dst_host_rerror_rate", "instances": 2052, "metric_value": 0.2707, "depth": 15}
                                             if obj[14]<=0.11883181316631937:
                                                return 'probe'
                                             else:
                                                return 'probe'
                                          else:
                                             return 'probe'
                                       else:
                                          return 'probe'
                                    else:
                                       return 'probe'
                                 else:
                                    return 'probe'
                              else:
                                 return 'probe'
                           else:
                              return 'probe'
                        elif obj[8]>115.65300500900987:
                           # {"feature": "flag", "instances": 836, "metric_value": 0.1879, "depth": 9}
                           if obj[2]>6.97999571336715:
                              # {"feature": "src_bytes", "instances": 836, "metric_value": 0.1879, "depth": 10}
                              if obj[3]>0:
                                 # {"feature": "count", "instances": 836, "metric_value": 0.1879, "depth": 11}
                                 if obj[4]<=84.1075547934875:
                                    # {"feature": "serror_rate", "instances": 836, "metric_value": 0.1879, "depth": 12}
                                    if obj[5]<=0.7309383846979811:
                                       # {"feature": "dst_host_count", "instances": 836, "metric_value": 0.1879, "depth": 13}
                                       if obj[7]<=182.14894461511594:
                                          # {"feature": "dst_host_same_src_port_rate", "instances": 836, "metric_value": 0.1879, "depth": 14}
                                          if obj[11]>0.7663706668194779:
                                             # {"feature": "dst_host_rerror_rate", "instances": 836, "metric_value": 0.1879, "depth": 15}
                                             if obj[14]<=0.11883181316631937:
                                                return 'probe'
                                             else:
                                                return 'probe'
                                          else:
                                             return 'probe'
                                       else:
                                          return 'probe'
                                    else:
                                       return 'probe'
                                 else:
                                    return 'probe'
                              else:
                                 return 'probe'
                           else:
                              return 'probe'
                        else:
                           return 'probe'
                     elif obj[9]<=0.5212416946488446:
                        # {"feature": "dst_host_count", "instances": 9, "metric_value": 1.5305, "depth": 8}
                        if obj[7]<=182.14894461511594:
                           # {"feature": "dst_host_srv_count", "instances": 7, "metric_value": 1.5567, "depth": 9}
                           if obj[8]<=115.65300500900987:
                              # {"feature": "flag", "instances": 4, "metric_value": 0.8113, "depth": 10}
                              if obj[2]>6.97999571336715:
                                 # {"feature": "src_bytes", "instances": 4, "metric_value": 0.8113, "depth": 11}
                                 if obj[3]>0:
                                    # {"feature": "count", "instances": 4, "metric_value": 0.8113, "depth": 12}
                                    if obj[4]<=84.1075547934875:
                                       # {"feature": "serror_rate", "instances": 4, "metric_value": 0.8113, "depth": 13}
                                       if obj[5]<=0.7309383846979811:
                                          # {"feature": "dst_host_same_src_port_rate", "instances": 4, "metric_value": 0.8113, "depth": 14}
                                          if obj[11]<=0.7663706668194779:
                                             # {"feature": "dst_host_rerror_rate", "instances": 4, "metric_value": 0.8113, "depth": 15}
                                             if obj[14]<=0.11883181316631937:
                                                return 'dos'
                                             else:
                                                return 'dos'
                                          else:
                                             return 'dos'
                                       else:
                                          return 'dos'
                                    else:
                                       return 'dos'
                                 else:
                                    return 'dos'
                              else:
                                 return 'dos'
                           elif obj[8]>115.65300500900987:
                              # {"feature": "flag", "instances": 3, "metric_value": 0.9183, "depth": 10}
                              if obj[2]>6.97999571336715:
                                 # {"feature": "src_bytes", "instances": 3, "metric_value": 0.9183, "depth": 11}
                                 if obj[3]>0:
                                    # {"feature": "count", "instances": 3, "metric_value": 0.9183, "depth": 12}
                                    if obj[4]<=84.1075547934875:
                                       # {"feature": "serror_rate", "instances": 3, "metric_value": 0.9183, "depth": 13}
                                       if obj[5]<=0.7309383846979811:
                                          # {"feature": "dst_host_same_src_port_rate", "instances": 3, "metric_value": 0.9183, "depth": 14}
                                          if obj[11]<=0.7663706668194779:
                                             # {"feature": "dst_host_rerror_rate", "instances": 3, "metric_value": 0.9183, "depth": 15}
                                             if obj[14]<=0.11883181316631937:
                                                return 'probe'
                                             else:
                                                return 'probe'
                                          else:
                                             return 'probe'
                                       else:
                                          return 'probe'
                                    else:
                                       return 'probe'
                                 else:
                                    return 'probe'
                              else:
                                 return 'probe'
                           else:
                              return 'probe'
                        elif obj[7]>182.14894461511594:
                           return 'probe'
                        else:
                           return 'probe'
                     else:
                        return 'probe'
                  elif obj[6]>0.0:
                     # {"feature": "dst_host_same_srv_rate", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[9]<=0.5212416946488446:
                        return 'normal'
                     elif obj[9]>0.5212416946488446:
                        return 'probe'
                     else:
                        return 'probe'
                  else:
                     return 'normal'
               elif obj[10]>0.6497142587290661:
                  # {"feature": "dst_host_srv_count", "instances": 14, "metric_value": 0.7496, "depth": 6}
                  if obj[8]<=115.65300500900987:
                     # {"feature": "dst_host_same_srv_rate", "instances": 13, "metric_value": 0.6194, "depth": 7}
                     if obj[9]<=0.5212416946488446:
                        # {"feature": "flag", "instances": 9, "metric_value": 0.7642, "depth": 8}
                        if obj[2]>6.97999571336715:
                           # {"feature": "src_bytes", "instances": 9, "metric_value": 0.7642, "depth": 9}
                           if obj[3]>0:
                              # {"feature": "count", "instances": 9, "metric_value": 0.7642, "depth": 10}
                              if obj[4]<=84.1075547934875:
                                 # {"feature": "serror_rate", "instances": 9, "metric_value": 0.7642, "depth": 11}
                                 if obj[5]<=0.7309383846979811:
                                    # {"feature": "diff_srv_rate", "instances": 9, "metric_value": 0.7642, "depth": 12}
                                    if obj[6]<=0.0:
                                       # {"feature": "dst_host_count", "instances": 9, "metric_value": 0.7642, "depth": 13}
                                       if obj[7]<=182.14894461511594:
                                          # {"feature": "dst_host_same_src_port_rate", "instances": 9, "metric_value": 0.7642, "depth": 14}
                                          if obj[11]<=0.7663706668194779:
                                             # {"feature": "dst_host_rerror_rate", "instances": 9, "metric_value": 0.7642, "depth": 15}
                                             if obj[14]<=0.11883181316631937:
                                                return 'dos'
                                             else:
                                                return 'dos'
                                          else:
                                             return 'dos'
                                       else:
                                          return 'dos'
                                    else:
                                       return 'dos'
                                 else:
                                    return 'dos'
                              else:
                                 return 'dos'
                           else:
                              return 'dos'
                        else:
                           return 'dos'
                     elif obj[9]>0.5212416946488446:
                        return 'dos'
                     else:
                        return 'dos'
                  elif obj[8]>115.65300500900987:
                     return 'probe'
                  else:
                     return 'probe'
               else:
                  return 'dos'
            elif obj[1]>31.22646916402721:
               return 'normal'
            else:
               return 'normal'
         elif obj[0]>0:
            # {"feature": "dst_host_diff_srv_rate", "instances": 747, "metric_value": 1.2337, "depth": 4}
            if obj[10]<=0.6497142587290661:
               # {"feature": "dst_host_same_src_port_rate", "instances": 411, "metric_value": 0.5102, "depth": 5}
               if obj[11]<=0.7663706668194779:
                  # {"feature": "diff_srv_rate", "instances": 285, "metric_value": 0.1179, "depth": 6}
                  if obj[6]<=0.0:
                     # {"feature": "dst_host_rerror_rate", "instances": 257, "metric_value": 0.0735, "depth": 7}
                     if obj[14]<=0.11883181316631937:
                        # {"feature": "dst_host_same_srv_rate", "instances": 238, "metric_value": 0.0392, "depth": 8}
                        if obj[9]<=0.5212416946488446:
                           return 'normal'
                        elif obj[9]>0.5212416946488446:
                           # {"feature": "service", "instances": 11, "metric_value": 0.4395, "depth": 9}
                           if obj[1]<=31.22646916402721:
                              return 'normal'
                           elif obj[1]>31.22646916402721:
                              # {"feature": "src_bytes", "instances": 5, "metric_value": 0.7219, "depth": 10}
                              if obj[3]>0:
                                 # {"feature": "flag", "instances": 4, "metric_value": 0.8113, "depth": 11}
                                 if obj[2]>6.97999571336715:
                                    # {"feature": "count", "instances": 4, "metric_value": 0.8113, "depth": 12}
                                    if obj[4]<=84.1075547934875:
                                       # {"feature": "serror_rate", "instances": 4, "metric_value": 0.8113, "depth": 13}
                                       if obj[5]<=0.7309383846979811:
                                          # {"feature": "dst_host_count", "instances": 4, "metric_value": 0.8113, "depth": 14}
                                          if obj[7]<=182.14894461511594:
                                             # {"feature": "dst_host_srv_count", "instances": 4, "metric_value": 0.8113, "depth": 15}
                                             if obj[8]<=115.65300500900987:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          else:
                                             return 'normal'
                                       else:
                                          return 'normal'
                                    else:
                                       return 'normal'
                                 else:
                                    return 'normal'
                              elif obj[3]<=0:
                                 return 'normal'
                              else:
                                 return 'normal'
                           else:
                              return 'normal'
                        else:
                           return 'normal'
                     elif obj[14]>0.11883181316631937:
                        # {"feature": "dst_host_same_srv_rate", "instances": 19, "metric_value": 0.2975, "depth": 8}
                        if obj[9]>0.5212416946488446:
                           return 'normal'
                        elif obj[9]<=0.5212416946488446:
                           # {"feature": "flag", "instances": 3, "metric_value": 0.9183, "depth": 9}
                           if obj[2]>6.97999571336715:
                              return 'normal'
                           elif obj[2]<=6.97999571336715:
                              return 'probe'
                           else:
                              return 'probe'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[6]>0.0:
                     # {"feature": "service", "instances": 28, "metric_value": 0.3712, "depth": 7}
                     if obj[1]>31.22646916402721:
                        # {"feature": "flag", "instances": 18, "metric_value": 0.3095, "depth": 8}
                        if obj[2]>6.97999571336715:
                           # {"feature": "src_bytes", "instances": 18, "metric_value": 0.3095, "depth": 9}
                           if obj[3]>0:
                              # {"feature": "count", "instances": 18, "metric_value": 0.3095, "depth": 10}
                              if obj[4]<=84.1075547934875:
                                 # {"feature": "serror_rate", "instances": 18, "metric_value": 0.3095, "depth": 11}
                                 if obj[5]<=0.7309383846979811:
                                    # {"feature": "dst_host_count", "instances": 18, "metric_value": 0.3095, "depth": 12}
                                    if obj[7]<=182.14894461511594:
                                       # {"feature": "dst_host_srv_count", "instances": 18, "metric_value": 0.3095, "depth": 13}
                                       if obj[8]<=115.65300500900987:
                                          # {"feature": "dst_host_same_srv_rate", "instances": 18, "metric_value": 0.3095, "depth": 14}
                                          if obj[9]<=0.5212416946488446:
                                             # {"feature": "dst_host_rerror_rate", "instances": 18, "metric_value": 0.3095, "depth": 15}
                                             if obj[14]<=0.11883181316631937:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          else:
                                             return 'normal'
                                       else:
                                          return 'normal'
                                    else:
                                       return 'normal'
                                 else:
                                    return 'normal'
                              else:
                                 return 'normal'
                           else:
                              return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=31.22646916402721:
                        # {"feature": "flag", "instances": 10, "metric_value": 0.469, "depth": 8}
                        if obj[2]>6.97999571336715:
                           # {"feature": "src_bytes", "instances": 10, "metric_value": 0.469, "depth": 9}
                           if obj[3]>0:
                              # {"feature": "count", "instances": 10, "metric_value": 0.469, "depth": 10}
                              if obj[4]<=84.1075547934875:
                                 # {"feature": "serror_rate", "instances": 10, "metric_value": 0.469, "depth": 11}
                                 if obj[5]<=0.7309383846979811:
                                    # {"feature": "dst_host_count", "instances": 10, "metric_value": 0.469, "depth": 12}
                                    if obj[7]<=182.14894461511594:
                                       # {"feature": "dst_host_srv_count", "instances": 10, "metric_value": 0.469, "depth": 13}
                                       if obj[8]<=115.65300500900987:
                                          # {"feature": "dst_host_same_srv_rate", "instances": 10, "metric_value": 0.469, "depth": 14}
                                          if obj[9]<=0.5212416946488446:
                                             # {"feature": "dst_host_rerror_rate", "instances": 10, "metric_value": 0.469, "depth": 15}
                                             if obj[14]<=0.11883181316631937:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          else:
                                             return 'normal'
                                       else:
                                          return 'normal'
                                    else:
                                       return 'normal'
                                 else:
                                    return 'normal'
                              else:
                                 return 'normal'
                           else:
                              return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               elif obj[11]>0.7663706668194779:
                  # {"feature": "diff_srv_rate", "instances": 126, "metric_value": 0.9617, "depth": 6}
                  if obj[6]<=0.0:
                     # {"feature": "service", "instances": 122, "metric_value": 0.8624, "depth": 7}
                     if obj[1]>31.22646916402721:
                        # {"feature": "flag", "instances": 64, "metric_value": 0.316, "depth": 8}
                        if obj[2]>6.97999571336715:
                           # {"feature": "src_bytes", "instances": 63, "metric_value": 0.3199, "depth": 9}
                           if obj[3]>0:
                              # {"feature": "count", "instances": 63, "metric_value": 0.3199, "depth": 10}
                              if obj[4]<=84.1075547934875:
                                 # {"feature": "serror_rate", "instances": 63, "metric_value": 0.3199, "depth": 11}
                                 if obj[5]<=0.7309383846979811:
                                    # {"feature": "dst_host_count", "instances": 63, "metric_value": 0.3199, "depth": 12}
                                    if obj[7]<=182.14894461511594:
                                       # {"feature": "dst_host_srv_count", "instances": 63, "metric_value": 0.3199, "depth": 13}
                                       if obj[8]<=115.65300500900987:
                                          # {"feature": "dst_host_same_srv_rate", "instances": 63, "metric_value": 0.3199, "depth": 14}
                                          if obj[9]>0.5212416946488446:
                                             # {"feature": "dst_host_rerror_rate", "instances": 63, "metric_value": 0.3199, "depth": 15}
                                             if obj[14]<=0.11883181316631937:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          else:
                                             return 'normal'
                                       else:
                                          return 'normal'
                                    else:
                                       return 'normal'
                                 else:
                                    return 'normal'
                              else:
                                 return 'normal'
                           else:
                              return 'normal'
                        elif obj[2]<=6.97999571336715:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=31.22646916402721:
                        # {"feature": "flag", "instances": 58, "metric_value": 0.9862, "depth": 8}
                        if obj[2]>6.97999571336715:
                           # {"feature": "src_bytes", "instances": 42, "metric_value": 0.9737, "depth": 9}
                           if obj[3]>0:
                              # {"feature": "count", "instances": 41, "metric_value": 0.9789, "depth": 10}
                              if obj[4]<=84.1075547934875:
                                 # {"feature": "serror_rate", "instances": 41, "metric_value": 0.9789, "depth": 11}
                                 if obj[5]<=0.7309383846979811:
                                    # {"feature": "dst_host_count", "instances": 41, "metric_value": 0.9789, "depth": 12}
                                    if obj[7]<=182.14894461511594:
                                       # {"feature": "dst_host_srv_count", "instances": 41, "metric_value": 0.9789, "depth": 13}
                                       if obj[8]<=115.65300500900987:
                                          # {"feature": "dst_host_same_srv_rate", "instances": 41, "metric_value": 0.9789, "depth": 14}
                                          if obj[9]>0.5212416946488446:
                                             # {"feature": "dst_host_rerror_rate", "instances": 41, "metric_value": 0.9789, "depth": 15}
                                             if obj[14]<=0.11883181316631937:
                                                return 'r2l'
                                             else:
                                                return 'r2l'
                                          else:
                                             return 'r2l'
                                       else:
                                          return 'r2l'
                                    else:
                                       return 'r2l'
                                 else:
                                    return 'r2l'
                              else:
                                 return 'r2l'
                           elif obj[3]<=0:
                              return 'r2l'
                           else:
                              return 'r2l'
                        elif obj[2]<=6.97999571336715:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[6]>0.0:
                     # {"feature": "src_bytes", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[3]<=0:
                        return 'u2r'
                     elif obj[3]>0:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'u2r'
               else:
                  return 'normal'
            elif obj[10]>0.6497142587290661:
               # {"feature": "src_bytes", "instances": 336, "metric_value": 0.3373, "depth": 5}
               if obj[3]<=0:
                  return 'probe'
               elif obj[3]>0:
                  # {"feature": "dst_host_rerror_rate", "instances": 22, "metric_value": 0.2668, "depth": 6}
                  if obj[14]<=0.11883181316631937:
                     return 'normal'
                  elif obj[14]>0.11883181316631937:
                     # {"feature": "service", "instances": 6, "metric_value": 0.65, "depth": 7}
                     if obj[1]<=31.22646916402721:
                        return 'normal'
                     elif obj[1]>31.22646916402721:
                        # {"feature": "flag", "instances": 3, "metric_value": 0.9183, "depth": 8}
                        if obj[2]>6.97999571336715:
                           # {"feature": "count", "instances": 3, "metric_value": 0.9183, "depth": 9}
                           if obj[4]<=84.1075547934875:
                              # {"feature": "serror_rate", "instances": 3, "metric_value": 0.9183, "depth": 10}
                              if obj[5]<=0.7309383846979811:
                                 # {"feature": "diff_srv_rate", "instances": 3, "metric_value": 0.9183, "depth": 11}
                                 if obj[6]<=0.0:
                                    # {"feature": "dst_host_count", "instances": 3, "metric_value": 0.9183, "depth": 12}
                                    if obj[7]<=182.14894461511594:
                                       # {"feature": "dst_host_srv_count", "instances": 3, "metric_value": 0.9183, "depth": 13}
                                       if obj[8]<=115.65300500900987:
                                          # {"feature": "dst_host_same_srv_rate", "instances": 3, "metric_value": 0.9183, "depth": 14}
                                          if obj[9]<=0.5212416946488446:
                                             # {"feature": "dst_host_same_src_port_rate", "instances": 3, "metric_value": 0.9183, "depth": 15}
                                             if obj[11]<=0.7663706668194779:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          else:
                                             return 'normal'
                                       else:
                                          return 'normal'
                                    else:
                                       return 'normal'
                                 else:
                                    return 'normal'
                              else:
                                 return 'normal'
                           else:
                              return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            else:
               return 'probe'
         else:
            return 'normal'
      else:
         return 'probe'
   elif obj[13]>0.7292347469535909:
      # {"feature": "flag", "instances": 35021, "metric_value": 0.1657, "depth": 2}
      if obj[2]<=6.97999571336715:
         # {"feature": "src_bytes", "instances": 34355, "metric_value": 0.0188, "depth": 3}
         if obj[3]<=0:
            # {"feature": "dst_host_same_src_port_rate", "instances": 34333, "metric_value": 0.0127, "depth": 4}
            if obj[11]<=0.7663706668194779:
               # {"feature": "dst_host_srv_count", "instances": 34299, "metric_value": 0.0083, "depth": 5}
               if obj[8]<=115.65300500900987:
                  # {"feature": "serror_rate", "instances": 34184, "metric_value": 0.0013, "depth": 6}
                  if obj[5]>0.7309383846979811:
                     return 'dos'
                  elif obj[5]<=0.7309383846979811:
                     # {"feature": "diff_srv_rate", "instances": 41, "metric_value": 0.3776, "depth": 7}
                     if obj[6]>0.0:
                        return 'dos'
                     elif obj[6]<=0.0:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'dos'
               elif obj[8]>115.65300500900987:
                  # {"feature": "dst_host_same_srv_rate", "instances": 115, "metric_value": 0.6858, "depth": 6}
                  if obj[9]<=0.5212416946488446:
                     # {"feature": "dst_host_diff_srv_rate", "instances": 95, "metric_value": 0.0843, "depth": 7}
                     if obj[10]<=0.6497142587290661:
                        return 'dos'
                     elif obj[10]>0.6497142587290661:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[9]>0.5212416946488446:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'dos'
            elif obj[11]>0.7663706668194779:
               # {"feature": "dst_host_srv_count", "instances": 34, "metric_value": 0.99, "depth": 5}
               if obj[8]<=115.65300500900987:
                  # {"feature": "diff_srv_rate", "instances": 28, "metric_value": 0.9059, "depth": 6}
                  if obj[6]<=0.0:
                     # {"feature": "service", "instances": 24, "metric_value": 0.9544, "depth": 7}
                     if obj[1]<=31.22646916402721:
                        # {"feature": "dst_host_srv_diff_host_rate", "instances": 22, "metric_value": 0.9457, "depth": 8}
                        if obj[12]>0.37023252388068995:
                           # {"feature": "protocol_type", "instances": 15, "metric_value": 0.971, "depth": 9}
                           if obj[0]>0:
                              # {"feature": "count", "instances": 15, "metric_value": 0.971, "depth": 10}
                              if obj[4]<=84.1075547934875:
                                 # {"feature": "serror_rate", "instances": 15, "metric_value": 0.971, "depth": 11}
                                 if obj[5]>0.7309383846979811:
                                    # {"feature": "dst_host_count", "instances": 15, "metric_value": 0.971, "depth": 12}
                                    if obj[7]<=182.14894461511594:
                                       # {"feature": "dst_host_same_srv_rate", "instances": 15, "metric_value": 0.971, "depth": 13}
                                       if obj[9]>0.5212416946488446:
                                          # {"feature": "dst_host_diff_srv_rate", "instances": 15, "metric_value": 0.971, "depth": 14}
                                          if obj[10]<=0.6497142587290661:
                                             # {"feature": "dst_host_rerror_rate", "instances": 15, "metric_value": 0.971, "depth": 15}
                                             if obj[14]<=0.11883181316631937:
                                                return 'dos'
                                             else:
                                                return 'dos'
                                          else:
                                             return 'dos'
                                       else:
                                          return 'dos'
                                    else:
                                       return 'dos'
                                 else:
                                    return 'dos'
                              else:
                                 return 'dos'
                           else:
                              return 'dos'
                        elif obj[12]<=0.37023252388068995:
                           # {"feature": "protocol_type", "instances": 7, "metric_value": 0.8631, "depth": 9}
                           if obj[0]>0:
                              # {"feature": "count", "instances": 7, "metric_value": 0.8631, "depth": 10}
                              if obj[4]<=84.1075547934875:
                                 # {"feature": "serror_rate", "instances": 7, "metric_value": 0.8631, "depth": 11}
                                 if obj[5]>0.7309383846979811:
                                    # {"feature": "dst_host_count", "instances": 7, "metric_value": 0.8631, "depth": 12}
                                    if obj[7]<=182.14894461511594:
                                       # {"feature": "dst_host_same_srv_rate", "instances": 7, "metric_value": 0.8631, "depth": 13}
                                       if obj[9]>0.5212416946488446:
                                          # {"feature": "dst_host_diff_srv_rate", "instances": 7, "metric_value": 0.8631, "depth": 14}
                                          if obj[10]<=0.6497142587290661:
                                             # {"feature": "dst_host_rerror_rate", "instances": 7, "metric_value": 0.8631, "depth": 15}
                                             if obj[14]<=0.11883181316631937:
                                                return 'dos'
                                             else:
                                                return 'dos'
                                          else:
                                             return 'dos'
                                       else:
                                          return 'dos'
                                    else:
                                       return 'dos'
                                 else:
                                    return 'dos'
                              else:
                                 return 'dos'
                           else:
                              return 'dos'
                        else:
                           return 'dos'
                     elif obj[1]>31.22646916402721:
                        # {"feature": "protocol_type", "instances": 2, "metric_value": 1.0, "depth": 8}
                        if obj[0]>0:
                           # {"feature": "count", "instances": 2, "metric_value": 1.0, "depth": 9}
                           if obj[4]<=84.1075547934875:
                              # {"feature": "serror_rate", "instances": 2, "metric_value": 1.0, "depth": 10}
                              if obj[5]>0.7309383846979811:
                                 # {"feature": "dst_host_count", "instances": 2, "metric_value": 1.0, "depth": 11}
                                 if obj[7]<=182.14894461511594:
                                    # {"feature": "dst_host_same_srv_rate", "instances": 2, "metric_value": 1.0, "depth": 12}
                                    if obj[9]>0.5212416946488446:
                                       # {"feature": "dst_host_diff_srv_rate", "instances": 2, "metric_value": 1.0, "depth": 13}
                                       if obj[10]<=0.6497142587290661:
                                          # {"feature": "dst_host_srv_diff_host_rate", "instances": 2, "metric_value": 1.0, "depth": 14}
                                          if obj[12]<=0.37023252388068995:
                                             # {"feature": "dst_host_rerror_rate", "instances": 2, "metric_value": 1.0, "depth": 15}
                                             if obj[14]<=0.11883181316631937:
                                                return 'normal'
                                             else:
                                                return 'normal'
                                          else:
                                             return 'normal'
                                       else:
                                          return 'normal'
                                    else:
                                       return 'normal'
                                 else:
                                    return 'normal'
                              else:
                                 return 'normal'
                           else:
                              return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[6]>0.0:
                     return 'dos'
                  else:
                     return 'dos'
               elif obj[8]>115.65300500900987:
                  return 'normal'
               else:
                  return 'normal'
            else:
               return 'dos'
         elif obj[3]>0:
            return 'normal'
         else:
            return 'normal'
      elif obj[2]>6.97999571336715:
         # {"feature": "src_bytes", "instances": 666, "metric_value": 0.9968, "depth": 3}
         if obj[3]>0:
            # {"feature": "dst_host_same_src_port_rate", "instances": 415, "metric_value": 0.044, "depth": 4}
            if obj[11]<=0.7663706668194779:
               return 'normal'
            elif obj[11]>0.7663706668194779:
               # {"feature": "service", "instances": 10, "metric_value": 0.7219, "depth": 5}
               if obj[1]<=31.22646916402721:
                  # {"feature": "dst_host_srv_count", "instances": 9, "metric_value": 0.5033, "depth": 6}
                  if obj[8]>115.65300500900987:
                     return 'normal'
                  elif obj[8]<=115.65300500900987:
                     # {"feature": "dst_host_srv_diff_host_rate", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[12]>0.37023252388068995:
                        return 'normal'
                     elif obj[12]<=0.37023252388068995:
                        return 'r2l'
                     else:
                        return 'r2l'
                  else:
                     return 'normal'
               elif obj[1]>31.22646916402721:
                  return 'r2l'
               else:
                  return 'r2l'
            else:
               return 'normal'
         elif obj[3]<=0:
            # {"feature": "dst_host_same_srv_rate", "instances": 251, "metric_value": 0.2078, "depth": 4}
            if obj[9]<=0.5212416946488446:
               # {"feature": "dst_host_diff_srv_rate", "instances": 249, "metric_value": 0.1419, "depth": 5}
               if obj[10]>0.6497142587290661:
                  # {"feature": "serror_rate", "instances": 245, "metric_value": 0.0383, "depth": 6}
                  if obj[5]>0.7309383846979811:
                     return 'probe'
                  elif obj[5]<=0.7309383846979811:
                     # {"feature": "service", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[1]>31.22646916402721:
                        return 'probe'
                     elif obj[1]<=31.22646916402721:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'probe'
               elif obj[10]<=0.6497142587290661:
                  return 'normal'
               else:
                  return 'normal'
            elif obj[9]>0.5212416946488446:
               return 'r2l'
            else:
               return 'r2l'
         else:
            return 'probe'
      else:
         return 'normal'
   else:
      return 'dos'
